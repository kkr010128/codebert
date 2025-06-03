import math
N,M,X = map(int,input().split())
#a[i][0]:price of the i-th book
a = [[] for i in range(N)]
for i in range(N):
    a[i] = list(map(int,input().split()))

def is_greater(b):
    for i in b:
        if i < X:
            return False
    return True 
    
cost = math.inf
for i in range(2**N):
    b = [0]*(M+1)
    for j in range(N):
        if ((i >> j)&1):
            for k in range(M+1):
                b[k] += a[j][k]
    if b[0] < cost and is_greater(b[1:]):
        cost = b[0]

if cost == math.inf:
    print(-1)
else:
    print(cost)