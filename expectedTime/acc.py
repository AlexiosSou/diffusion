from api import openACC
import numpy as np

#initialize
openACC(1)

def do(size:int):

    acc0=np.zeros(size)
    acc1=np.zeros(size)

    for i in range(size):
        acc0[i]=openACC(0)
        acc1[i]=openACC(1)

    m0=np.mean(acc0)
    std0=np.std(acc0)
    m1=np.mean(acc1)
    std1=np.std(acc1)

    print(f'openACC(0): mean: {m0}ms, deviation:{std0}ms')
    print(f'openACC(1): mean: {m1}ms, deviation:{std1}ms')
    
do(1000)