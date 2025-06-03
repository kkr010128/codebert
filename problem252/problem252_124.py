import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

MOD = 10 ** 9 +7

n,m = map(int,readline().split())
a = np.array(read().split(),np.int64)

a.sort()

def shake_cnt(x):
    X=np.searchsorted(a,x-a)
    return n*n-X.sum()

left = 0
right = 10 ** 6
while left+1 <right:
    x = (left + right)//2
    if shake_cnt(x) >= m:
        left = x
    else:
        right = x

left,right

X=np.searchsorted(a,right-a)
Acum = np.zeros(n+1,np.int64)
Acum[1:] = np.cumsum(a)

shake = n * n -X.sum()
happy = (Acum[-1]-Acum[X]).sum()+(a*(n-X)).sum()

happy += (m-shake)*left
print(happy)