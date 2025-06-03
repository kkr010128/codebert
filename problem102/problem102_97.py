import decimal
import numpy as np
import sys

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))

N,K = LI()
A = LI()

ans = []

for i in range(K,N):
    if A[i-K] < A[i]:
        ans.append('Yes')
    else:
        ans.append('No')

print('\n'.join(ans))