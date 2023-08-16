# Vehicle Upright Health Monitor



## Machine learning model made easy

The combination of machine learning, FEA and Racedynamics all rolled into one. The model leverages the usefulness of data from endurance runs and creates a visualisation of the stress distribution and serves to estimate the life/damage to the vehicle upright. A machine learning model learns the distribution of the stress as a function of the steering and the acceleration. The load cases are divided into acceleration, braking, cornering with acceleration, cornering with braking and cornering. A simple ANN based neural network generates a numpy array of stress that can be displayed as scalar values on a voxel 3D mesh. Pyvista library offers a powerful 3D visualising tool to visualise this data. This allows us to leverage the power of visualisation through data rather than building complex neural networks that needs to work through 3D meshes. 
To perform a demo of this app you can scan the following QR code.
(Caution: Run for a limited time less than 30s preferably to test process,fork the repo and use the power of your processors to utilise the maximum potential)
(Why? The demo is deployed on the streamlit community sharing which has limited memory)

![image](https://github.com/Mukund-Thirugnanasambanthar/Digital_Twin/assets/116257453/930cd0ee-7bda-44e6-8c70-4dbb6304d8f7)


## Steps to run the app:
* Fork the Repo.
* Perform a pip install of all the required libraries mentioned in requirements.txt
* Use the Acceleration_steering.py to create the numpy arrays for the input.
* Run the app by typing in the following code.
```
 python -m run streamlit Upright_Stress.py
```
* Upload the acceleration and the steering files, The uprightstress communicates the prediction.py and the life_predictor.py to compute and plot the results

### Use the model and get creative, the weights from the machine learning model are also given with the repo. There is a model code for a sample neural network that can be extended to the user case. By replacing the Voxel model definition in the Upright_stress.py this setup can be extended to other use cases. So like I mentioned try and get creative.
