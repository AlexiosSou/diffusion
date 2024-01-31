import numpy as np
import matplotlib.pyplot as plt

#manually input the time ratio corresponding to OMP_NUM_THREADS
axis=np.array([i for i in range(1,15)])
mean=np.array([1.007021207892581,2.0083634581189616,2.9995321003591626,3.9936965801617497,4.980219912174443,
              5.968316989639166,6.95838460043926,7.693171415408891,8.595365547275044,9.536459724770019,
              10.463915730232268,11.400789687285146,12.283414642312554,12.555062944784705])
std=np.array([0.0016122463702984541,0.0025876260542592737,0.005149258956029684,0.012484506783450014,
             0.019658553565903323,0.02088266159364655,0.02795066318087413,0.05475198421444389,
             0.10854503572144422,0.08741761745595594,0.08314355677284911,0.1066465409390292,
             0.12805349314688866,1.283267408425016])
parameter=3/np.sqrt(10)

CI=std*parameter

lowerBound=mean-CI
upperBound=mean+CI

plt.plot(axis,mean,color='b',label='mean')
plt.fill_between(axis,lowerBound,upperBound,color='g',label='3-sigma CI')
plt.title('Ratio of execution time to Seq by number of threads')
plt.xlabel('OMP_NUM_THREADS')
plt.legend()
plt.savefig('ratio.png')