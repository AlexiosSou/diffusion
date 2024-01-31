from api import sequential,openMP,openACC
import numpy as np
import matplotlib.pyplot as plt

def printTime(iteration:int):
    
    axis=[i for i in range(iteration)]
    time=[0.0 for i in range(iteration)]
    for i in range(iteration):
        res=openACC(1)
        time[i]=res
        print(f'The time for {i}-th iteration with OpenACC is {res}ms')
        
    plt.plot(axis,time)
    plt.title('Execution time of OpenACC for each iteration')
    plt.ylabel('Execution Time/ms')
    plt.savefig('initialACC.png')
    
printTime(1000)