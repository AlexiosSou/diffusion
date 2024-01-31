from api import sequential
import numpy as np

def do(size:int):

    samples=np.zeros(size)

    for i in range(size):
        samples[i]=sequential(1)

    m=np.mean(samples)
    CI=3*np.std(samples)/np.sqrt(size)

    print(f'sequential(1): mean: {m}ms, CI:{CI}ms')
    
do(10)