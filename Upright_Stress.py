import numpy as np
import pyvista as pv
import pandas as pd
from pyvista import CellType
from stpyvista import stpyvista
import streamlit as st
from prediction import predict
import matplotlib.pyplot as plt
import matplotlib as mpl
import altair as alt
from PIL import Image
st.set_page_config(page_title="Vehicle Upright Health Monitor",layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)
image=Image.open('Logo.png')
image.resize([700,87])
H_col1,H_col2,H_col3=st.columns(3)
with H_col1:
    st.image(image)
    st.subheader("Vehicle Upright Stress Plot")
with H_col2:
    upload_accel_file=st.file_uploader("Choose Acceleration file")
    if upload_accel_file is not None:
        acceleration=np.load(upload_accel_file)
with H_col3:
    upload_steering_file=st.file_uploader("Choose Steering file")
    if upload_steering_file is not None:
        steering=np.load(upload_steering_file) 
Col1,Col2=st.columns([0.25,0.75])
with Col1:
    time=st.number_input('Time Frame to compute')
    time=int(time)
    x=np.arange(0,time,1)
    # st.write(len(acceleration),np.shape(x))
    # figure,(ax_1,ax_2)=plt.subplots(2,1,figsize=(20,4))
    # ax_1.plot(x,acceleration)
    # ax_2.plot(x,steering)
    # st.pyplot(figure)
    number=st.slider('Index',min_value=0, max_value=time, value=None, step=1)
    chart_data=pd.DataFrame({'x':x,'Acceleration':acceleration[0:time],'Steering':steering[0:time]})
    chart_accel=(alt.Chart(chart_data).mark_trail(point=True).encode(x='x',y='Acceleration',color=alt.condition(alt.datum.x==number,alt.value('orange'),alt.value('steelblue')))).properties(width=1800, height=150)
    chart_steering=(alt.Chart(chart_data).mark_trail(point=True).encode(x='x',y='Steering',color=alt.condition(alt.datum.x==number,alt.value('orange'),alt.value('steelblue')))).properties(width=1800, height=150)
    st.altair_chart(chart_accel,use_container_width=True)
    st.altair_chart(chart_steering,use_container_width=True)
    st.subheader("Acceleration:"+str(acceleration[number]))
    st.subheader('Steering:'+str(steering[number]))
    predictor_button=st.button("Predict Stress Distribution")
fem_file=open('E13_FEMModel.fem','r')
content=fem_file.read()
splitted_line=content.splitlines()
Grid=[]
iter=0
for i in splitted_line:
    if i.find('GRID')==0:
        iter=iter+1
        Grid.append(float(i[24:32]))
        Grid.append(float(i[32:40]))
        Grid.append(float(i[40:48]))
    else:
        continue
Grid=np.array(Grid)
points=np.reshape(Grid,(iter,3))
Hexa_line=splitted_line[0:133563]
Hexa_iter=0
Hexa=[]
for j in Hexa_line:
    if (j.find('CHEXA')==0):
        #Hexa.append(int(j[20:25]))
        Hexa.append(int(j[27:33])-1)
        Hexa.append(int(j[35:41])-1)
        Hexa.append(int(j[43:49])-1)
        Hexa.append(int(j[51:57])-1)
        Hexa.append(int(j[59:65])-1)
        Hexa.append(int(j[67:73])-1)
        Hexa_iter=Hexa_iter+1
    elif (j.find('+')==0):
        Hexa.append(int(j[11:17])-1)
        Hexa.append(int(j[19:25])-1)
Hexa=np.array(Hexa)
Voxel=np.reshape(Hexa,(Hexa_iter,8))
# grid = pv.UnstructuredGrid(Voxel_,[CellType.HEXAHEDRON], data)
cell=[]
for k in range(0,Hexa_iter):
    cell_data=np.append(8,Voxel[k])
    cell.append(cell_data)
cells=np.array([cell])
# # print(cells[0])
# # print(np.shape(points))
celltypes=np.full(Hexa_iter,CellType.HEXAHEDRON,dtype=np.float32)
grid=pv.UnstructuredGrid(cells,celltypes,points)
# # # #grid=pv.StructuredGrid(points)
if acceleration[number] < 0 and steering[number] == 0:
    case="Case_1"
elif acceleration[number] > 0 and steering[number] == 0:
    case="Case_2"
elif acceleration[number] > 0 and steering[number] != 0:
    case="Case_4"
elif acceleration[number] < 0 and steering[number] != 0:
    case="Case_5"
elif steering[number] != 0:
    case="Case_3"
#case = st.selectbox('Case',('Case_1', 'Case_2', 'Case_3','Case_4','Case_5'))
with Col2:
    if predictor_button:
        col1,col2=st.columns([5,1])
        with col1:
            accel=abs(acceleration[number])
            result=predict([accel],case)
            grid.cell_data["values"] = result
            pyvista.start_xvfb()
            plotter=pv.Plotter(window_size=[700,500])
            plotter.view_isometric()
            plotter.add_axes(line_width=5)
            sargs = dict(interactive=True)
            plotter.add_mesh(grid,cmap='jet',show_edges=True,line_width=1,)
            plotter.add_scalar_bar("Stress",result,title_font_size=50,label_font_size=30,outline=True,fmt='%10.5f')
            #plotter.add_scalar_bar('Data')
            #plotter.add_scalar_bar['values']
            #st.pyvista_scene(plotter)
            #plotter.show()
            stpyvista(plotter,horizontal_align='center',panel_kwargs=dict(orientation_widget=True,add_scalar_bar="Data",show_scalar_bar=True))
        with col2:
            fig,ax = plt.subplots(figsize=(0.25,2))
            #ax = fig.add_axes([0.05, 0.80, 0.9, 0.1])
            vmax=float(max(result))
            vmin=float(min(result))
            #cb = mpl.colorbar.ColorbarBase(ax,cmap='jet',norm=mpl.colors.Normalize(vmin, vmax),ticks=[vmin,0.25*vmax,0.5*vmax, 0.75*vmax,vmax])
            norm = mpl.colors.Normalize(vmin, vmax)
            fraction=1
            cbar = ax.figure.colorbar(
                mpl.cm.ScalarMappable(norm=norm, cmap='jet'),
                ax=ax,fraction=fraction,ticks=[vmin,0.25*vmax,0.5*vmax, 0.75*vmax,vmax])
            ax.axis('off')
            legend=fig.savefig('Colorbar.png')
            st.pyplot(fig)
    acceleration_life=acceleration[0:time]
    steering_life=steering[0:time]
    max_stress=[]
    for i in range(len(acceleration_life)):
        if acceleration_life[i] < 0 and steering_life[i] == 0:
            case_life="Case_1"
        elif acceleration_life[i] > 0 and steering_life[i] == 0:
            case_life="Case_2"
        elif acceleration_life[i] > 0 and steering_life[i] != 0:
            case_life="Case_4"
        elif acceleration_life[i] < 0 and steering_life[i] != 0:
            case_life="Case_5"
        elif steering_life[i] != 0:
            case_life="Case_3"
        stress=predict([acceleration_life[i]],case_life)
        maxi=max(stress)
        max_stress.append(maxi)
    
    stresslevels_rice_Endurance_ksi = [element * 0.145 for element in max_stress]
    # Given Constants
    
    A_1 = 14.86
    A_2 = 5.80
    A_3 = 0.49
    A_4 = 0.0
    R_SNcurve = -1.0

    # Calculate S-equivalent
    S_equivalent_Endurance_ksi = [element * ((1- R_SNcurve)**A_3) for element in stresslevels_rice_Endurance_ksi]
    
    # Calculate log(Nf)
    log_Nf_Endurance_ksi = [A_1 - (A_2*np.log10(element - A_4)) for element in S_equivalent_Endurance_ksi]

    # Calculate Nf
    Nf_Endurance_ksi = [(10**element) for element in log_Nf_Endurance_ksi]

    # Assuming N_Endurance_ksi is the number of occurrences of each stress level
    # For our case, every stress level occurs once per second.
    N_Endurance_ksi = [1 for _ in stresslevels_rice_Endurance_ksi]
    # Calculate Damage
    Damage_Endurance_ksi_list = [i / j for i, j in zip(N_Endurance_ksi, Nf_Endurance_ksi)]
    Damage_Endurance_ksi = sum(Damage_Endurance_ksi_list)
    st.subheader("Damage for uploaded Run:" +str(round(float(Damage_Endurance_ksi*(10**12)),3))+str('e-12'))
    st.caption('Incase of any questions or feedback contact Mukund Thirugnanasambanthar(@MuTh on Slack) mukund.thirugnanasambanthar@greenteam-stuttgart.de')
        
