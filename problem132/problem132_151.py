import numpy as np
from numba import njit, prange

#'''
N, K = map(int, input().split())
As = list(map(int, input().split()))
'''
N = 200000
K = 100000
As = [0] * N
#'''

@njit("i8[:](i8[:],)", cache = True)
def update(A_array):
    before_csum = np.zeros(N+1, np.int64)
    for i, A in enumerate(A_array[:N]):
        before_csum[max(0, i-A)] += 1
        before_csum[min(N, i+A+1)] -= 1
    return np.cumsum(before_csum)
    
A_array = np.array(As + [0], dtype = np.int64)
for k in range(min(K, 50)):
    A_array = update(A_array)
    
print(*A_array.tolist()[:N])