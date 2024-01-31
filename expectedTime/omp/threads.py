import os

for i in range(1, 15):
    print(f'\n{i} threads working\n')
    os.system(f'OMP_NUM_THREADS={i} python3 ratio.py')