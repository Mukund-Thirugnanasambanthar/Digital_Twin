# Define the phases and their corresponding acceleration and steering values
import random
import numpy as np
phases = [(4, 3, 0), (8, 0, 0), (4, -2, 15), (4, 0, 15), (4, 2, 0), (8, 0, 0), (16, -1, 0), (16, 0, 0), (16, 1, 0)]

# Initialize empty lists to store the accelerations and steering angles
accelerations = []
steering_angles = []

# Repeat for each lap
for _ in range(18):
    # Add a random time delay to this lap
    time_delay = random.randint(0, 5)

    # Repeat for each phase
    for time, acceleration, steering_angle in phases:
        # Repeat for each second in the phase, plus the time delay
        for _ in range(time + time_delay):
            # Add the acceleration value and steering angle for that phase with some random noise
            accelerations.append(round(acceleration + random.uniform(-0.5, 0.5),1))
            steering_angles.append(round(steering_angle + random.uniform(-2, 2),1))

    # After adding the time delay to the lap, remove it from the following lap to maintain the total race time
    phases[0] = (phases[0][0] - time_delay, phases[0][1], phases[0][2])

accelerations=np.array(accelerations[:1382])
steering_angles=np.array(steering_angles[:1382])


# Print the accelerations and steering angles
print("Accelerations:", accelerations)
print("Steering Angles:", steering_angles)
np.save('C:/Users/Mukund/Documents/Digital_Twin/Voxel/acceleration.npy',accelerations)
np.save('C:/Users/Mukund/Documents/Digital_Twin/Voxel/steering_angle.npy',steering_angles)