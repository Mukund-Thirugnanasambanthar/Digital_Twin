#!/usr/bin/env python
# coding: utf-8

# # Model 1

# In[8]:


import pandas as pd
import numpy as np
import tensorflow as tf
import keras
from sklearn.model_selection import train_test_split
import cv2
from PIL import Image as img
import random
from matplotlib import image


# In[23]:


x=np.load("C:/Users/Mukund/Documents/Digital_Twin/Voxel/xcase1.npy")
values=np.load("C:/Users/Mukund/Documents/Digital_Twin/Voxel/ycase1.npy")
y=[]
for i in range(len(values)):
    y.append(values[i])
y=np.array(y)


# In[24]:


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=42)
print(len(X_test))
print(len(y_test))


# In[27]:


model1 = keras.Sequential([
    keras.layers.Dense(1,input_shape=(1,)),
    keras.layers.Dense(150, activation=tf.nn.relu),
    keras.layers.Dense(150, activation=tf.nn.relu),
    keras.layers.Dense(150, activation=tf.nn.relu),
    keras.layers.Dense(150, activation=tf.nn.relu),
    keras.layers.Dense(30255, activation=tf.nn.relu),
    keras.layers.Flatten()
])

model1.compile(optimizer='adam',loss='mean_squared_error',metrics=['mean_squared_error'])


# In[28]:


model1.fit(X_train,y_train,epochs=60, validation_data=(X_test,y_test),batch_size=1)


# In[30]:


test_loss, test_acc = model1.evaluate(X_test, y_test)
print(test_acc)


# In[31]:


model1.save('C:/Users/Mukund/Documents/Digital_Twin/Case1.json')


# In[32]:


pred=model1.predict([29.5])


# In[33]:


pred[0]


# In[36]:


print(y[294])


# In[37]:


import matplotlib.pyplot as plt


# In[40]:


x_axis=np.arange(0,30255,1)
fig, ax = plt.subplots()
ax.plot(x_axis, y[294], linewidth=2.0)
ax.plot(x_axis, pred[0], linewidth=2.0)


# In[41]:


model1.summary()


# In[ ]:




