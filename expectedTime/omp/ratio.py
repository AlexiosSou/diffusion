from api import sequential,openMP
import numpy as np
import matplotlib.pyplot as plt

def output(size:int):
    samples=np.zeros(size)
    for i in range(size):
        samples[i]=sequential(3)/openMP(3)
    m=np.mean(samples)
    std=np.std(samples)
    print(f'Mean for seq(3)/openMP(3) is {m}, deviation is {std}')

output(10)