import tensorflow as tf
import keras
import numpy as np

def predict(data,case):
    if case == 'Case_1':
        name = 'Case1.json'
    elif case == 'Case_2':
        name = 'Case2.json'
    elif case == 'Case_3':
        name = 'Case3.json'
    elif case == 'Case_4':
        name = 'Case4.json'
    elif case == 'Case_5':
        name = 'Case5.json'
    load_model=tf.keras.saving.load_model("C:/Users/Mukund/Documents/Digital_Twin/"+name)
    pred=load_model.predict(data)
    pred=np.array(pred)
    pred=np.reshape(pred,(30255,1))
    return pred

