import numpy as np
from numba import *


N = int(input())
length = np.array(input().split(), np.int64)


length = np.sort(length)


def calc(length):
    cnt = 0
    
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                l1, l2, l3 = length[i], length[j], length[k]
                if (l1 != l2 and l1 != l3 and l2 != l3):
                    if (l1 + l2 > l3):
                        cnt += 1
    
    return (cnt)

ans = calc(length)
print(ans)
