import tensorflow as tf
import keras
import numpy as np

def life(data,case):
    #max_stress=[]
    #for i in range(len(data)):
     #   if case[i] == 'Case_1':
      #      name = 'Case1.json'
       # elif case[i] == 'Case_2':
        #    name = 'Case2.json'
        #elif case[i] == 'Case_3':
         #   name = 'Case3.json'
        #elif case[i] == 'Case_4':
         #   name = 'Case4.json'
        #elif case[i] == 'Case_5':
         #   name = 'Case5.json'
        #load_model=tf.keras.saving.load_model(name)
        #pred=load_model.predict(data[i])
        #pred=np.array(pred)
        #pred=np.reshape(pred,(30255,1))
        #max_stress.append(max(pred))
    return len(data),len(case)
