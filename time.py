from api import sequential,openMP,openACC
import numpy as np
import matplotlib.pyplot as plt

def printTime(start:int,end:int,sampleSize:int):
    
    para=1/np.sqrt(sampleSize)
    
    #initialization
    openACC(1)
    openMP(1)
    sequential(1)
    
    iterations=[i for i in range(start,end)]
    
    meanA=[0.0 for i in range(start,end)]
    upperBoundA=[0.0 for i in range(start,end)]
    lowerBoundA=[0.0 for i in range(start,end)]

    meanM=[0.0 for i in range(start,end)]
    upperBoundM=[0.0 for i in range(start,end)]
    lowerBoundM=[0.0 for i in range(start,end)]
    
    meanS=[0.0 for i in range(start,end)]
    upperBoundS=[0.0 for i in range(start,end)]
    lowerBoundS=[0.0 for i in range(start,end)]
    
    for i in range(start,end):
        samples=np.zeros(sampleSize)
        #estimate OpenACC
        for j in range(sampleSize):
            samples[j]=openACC(i)
        
        m=np.mean(samples)
        std=np.std(samples)
        CI=3*std*para
        meanA[i-start]=m
        upperBoundA[i-start]=m+CI
        lowerBoundA[i-start]=m-CI
        
        #estimate OpenMP
        for j in range(sampleSize):
            samples[j]=openMP(i)
        
        m=np.mean(samples)
        std=np.std(samples)
        CI=3*std*para
        meanM[i-start]=m
        upperBoundM[i-start]=m+CI
        lowerBoundM[i-start]=m-CI
        
        #estimate Sequential
        for j in range(sampleSize):
            samples[j]=sequential(i)
            
        m=np.mean(samples)
        std=np.std(samples)
        CI=3*std*para
        meanS[i-start]=m
        upperBoundS[i-start]=m+CI
        lowerBoundS[i-start]=m-CI
    
    #plot OpenACC    
    plt.plot(iterations,meanA,label='OpenACC',color='r')
    plt.fill_between(iterations,lowerBoundA,upperBoundA,label=f'Asymptic 3-sigma CI for Execution Time of OpenACC',color='y')
    
    #plot OpenMP
    plt.plot(iterations,meanM,label='OpenMP',color='b')
    plt.fill_between(iterations,lowerBoundM,upperBoundM,label=f'Asymptic 3-sigma CI for Execution Time of OpenMP',color='g')
    
    #plot sequential
    plt.plot(iterations,meanS,label='sequential',color='k')
    plt.fill_between(iterations,lowerBoundS,upperBoundS,label=f'Asymptic 3-sigma CI for Execution Time of sequential',color='c')
    
    plt.title(f'Estimation of Execution Time')
    plt.xlabel('iteration')
    plt.ylabel('Execution Time/ms')
    plt.legend()
    plt.savefig(f'test.png')

printTime(2,10,100)