import numpy as np
n = int(input())
k = np.arange(1,n+1)
d = n // k
print((k*d*(d+1)//2).sum())