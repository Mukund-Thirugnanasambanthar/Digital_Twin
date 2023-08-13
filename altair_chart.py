import matplotlib.pyplot as plt
import matplotlib as mpl

fig = plt.figure()
ax = fig.add_axes([0.05, 0.80, 0.9, 0.1])
vmax=11.3371
vmin=0
cb = mpl.colorbar.ColorbarBase(ax, orientation='horizontal',cmap='jet',norm=mpl.colors.Normalize(vmin, vmax),ticks=[vmin,0.25*vmax,0.5*vmax, 0.75*vmax,vmax])
plt.show()