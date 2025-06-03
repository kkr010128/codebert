###2分探索

import sys

N,K = map(int,input().split())

A = list(map(int,input().split()))

p = 0###無理（そこまで小さくできない）
q = max(A)###可能

if K == 0:
    print(q)
    sys.exit(0)

while q-p > 1:
    r = (p+q)//2
    count = 0
    for i in range(N):
        if A[i]/r == A[i]//r:
            count += A[i]//r - 1
        else:
            count += A[i]//r
    if count > K:
        p = r
    else:
        q = r
    #print(p,q)

print(q)