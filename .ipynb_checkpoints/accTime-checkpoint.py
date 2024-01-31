from api import seqT,ompT,accT
import numpy as np
import matplotlib.pyplot as plt

def printTime(start:int,end:int,iteration:int,func):
    #initialization
    func(1)
    
    sizes=[i for i in range(start,end)]
    mean=[0.0 for i in range(start,end)]
    for i in range(start,end):
        samples=np.zeros(iteration)
        for j in range(iteration):
            samples[j]=func(i)
        mean[i-start]=np.mean(samples)
        
    plt.plot(sizes,mean)
    plt.title(f'Estimation of Execution Time with {func.__name__}')
    plt.xlabel('iteration')
    plt.ylabel('Execution Time/ms')
    plt.legend()
    plt.savefig(f'Estimation of Execution Time.png')

printTime(0,10,1,accT)