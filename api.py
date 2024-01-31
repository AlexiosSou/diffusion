from ctypes import CDLL, c_double, c_int

lib=CDLL('./diffusion.so')

#results are in microseconds
seq=lib.seqTime
seq.argtypes=[c_int]
seq.restype=c_double
omp=lib.ompTime
omp.argtypes=[c_int]
omp.restype=c_double
acc=lib.accTime
acc.argtypes=[c_int]
acc.restype=c_double

def sequential(n:int):
    return float(seq(n))/1000

def openMP(n:int):
    return float(omp(n))/1000

def openACC(n:int):
    return float(acc(n))/1000