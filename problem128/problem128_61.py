X,N=map(int,input().split())
*P,=sorted(map(int,input().split()))

from bisect import bisect_left

if N==0:
    t=X
else:
    l = bisect_left(P, X)
    for i in range(100):
        t=X-i
        if l-i<0 or t!=P[l-i]: break
        t=X+i
        if N<=l+i or t!=P[l+i]: break
print(t)