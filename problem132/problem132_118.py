import math
import numpy as np

n,k=(int(x) for x in input().split())
a = [int(x) for x in input().split()]


for _ in range(k):
    new_a = np.zeros(n+1,dtype=int)
    np.add.at(new_a, np.maximum(0,np.arange(0, n)-a), 1)
    np.add.at(new_a, np.minimum(n,np.arange(0, n)+a+1), -1)
    a = new_a.cumsum()[:-1]
    if np.all(a==n):
        break

print(" ".join([str(x) for x in a]))