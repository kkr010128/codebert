from sys import exit
import math
import collections
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

A,B,M = mi()
a = li()
b = li()
xyc = [li() for i in range(M)]

ans = min(a)+min(b)
for i in range(M):
    ans = min(ans,a[xyc[i][0]-1]+b[xyc[i][1]-1] - xyc[i][2])
print(ans)