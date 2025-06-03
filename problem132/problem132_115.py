
import numpy as np
from numba import njit

N_ko, K_kai = map(int, input().split())
A_list = list(map(int, input().split()))
A = np.array(A_list, dtype=np.int64)

@njit
def cal_cumsum(A):
    Light_length = np.zeros(N_ko, dtype=np.int64)
    
    for i in range(N_ko):
        left = max(0, i - A[i])
        right = min(N_ko - 1, i + A[i])
        
        Light_length[left] += 1
        
        if (right + 1 < N_ko):
            Light_length[right + 1] -= 1
    
    Light_length = np.cumsum(Light_length)

    return(Light_length)

for k in range(min(42, K_kai)):
    A = cal_cumsum(A)


print(*A)
