import csv
import pandas as pd
import numpy as np
rows = []
with open("C:/Users/Mukund/Documents/Digital_Twin/Voxel/330Case5.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
values=[]
for value in (rows):
    if len(value)==2:
        values.append(float(value[0]+'.'+value[1]))
    else:
        values.append(float(value[0]))
scalar_values=np.append(float(header[0]),values)
print(len(scalar_values))
case_1=np.reshape(scalar_values,((int(len(scalar_values)/30255),30255)))

case_1=case_1[3:]
print(case_1[320])
x=[]
for i in range(1,330):
    x.append(i/10)
x=np.array(x)
np.save('C:/Users/Mukund/Documents/Digital_Twin/Voxel/xcase5.npy',x)
np.save('C:/Users/Mukund/Documents/Digital_Twin/Voxel/ycase5.npy',case_1)