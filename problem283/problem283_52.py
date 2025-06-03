import math
import numpy as np

N = int(input())

N_half = math.floor(N/2)

counts = 0
for i in np.arange(1, N):
    j = N-i
    if(i != j ):
        counts += 1
        
print(int(counts/2))