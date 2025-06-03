import numpy as np
import sys 
N,K = map(int, input().split())
A = np.array(sys.stdin.readline().split(), np.int64)
maxa = np.max(A)
mina = maxa // (K+1)
while maxa > mina + 1:
    mid = (maxa + mina)// 2
    div = np.sum(np.ceil(A/mid-1))
    if div > K:
        mina = mid
    else:
        maxa = mid

print(maxa)

