# Kalman Filtering

The demonstration has two different sections. The first section creates simulated data. The second section runs a Kalman filter on the data and visualizes the results.

### Kalman Filters - Why are they useful?

Kalman filters are really good at taking noisy sensor data and smoothing out the data to make more accurate predictions. For autonomous vehicles, Kalman filters can be used in object tracking. 


### Kalman Filters and Sensors
Object tracking is often done with radar and lidar sensors placed around the vehicle. A radar sensor can directly measure the distance and velocity of objects moving around the vehicle. A lidar sensor only measures distance.

Put aside a Kalman filter for a minute and think about how we could use lidar data to track an object. Let's say there is a bicyclist riding around in front of us. We send out a lidar signal and receive the signal back. The lidar sensor tells us that the bicycle is 10 meters directly ahead of us but gives no velocity information.

By the time our lidar device sends out another signal, maybe 0.05 seconds will have passed. But during those 0.05 seconds, our vehicle still needs to keep track of the bicycle. So our vehicle will predict where it thinks the bycicle will be. But our vehicle has no bicycle velocity information.

After 0.05 seconds, the lidar device sends out and receives another signal. This time, the bicycle is 9.95 meters ahead of us. Now we know that the bicycle is traveling -1 meter per second towards us. For the next 0.05 seconds, our vehicle will assume the bicycle is traveling -1 m/s towards us. Then another lidar signal goes out and comes back, and we can update the position and velocity again.

### Sensor Noise
Unfortunately, lidar and radar signals are noisy. In other words, they are somewhat inacurrate. A Kalman filter helps to smooth out the noise so that we get a better fix on the bicycle's true position and velocity. 

A Kalman filter does this by weighing the uncertainty in our belief about the location versus the uncertainty in the lidar or radar measurement. If our belief is very uncertain, the Kalman filter gives more weight to the sensor. If the sensor measurement has more uncertainty, our belief about the location gets more weight than the sensor measurement. 
