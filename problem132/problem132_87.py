import numpy as np
from numba import njit

n,k =map(int,input().split())
a= np.array(list(map(int,input().split())))

@njit(cache=True)
def light(n,a_list):
    outcome= np.zeros(n+1, dtype=np.int64)
    for i in range(n):
        outcome[max(0,i-a_list[i])] += 1
        outcome[min(n,i+a_list[i]+1)] -= 1
    outcome = np.cumsum(outcome)[:-1]
    return outcome

for _ in range(k):
    if min(a) == n:
        break
    a = light(n,a)

[print(aa,end=' ') for aa in a]