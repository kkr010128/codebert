ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
n,m = ma()
s = input()
dp = [-1]*(n+1) #dp[i]:: i番目にたどり着く最小コスト
dp[0]=0
r=0
while r<=n-1:
    l=0
    tmp=0
    while l+1<=m and r+l+1<=n:
        l+=1
        if s[r+l]=="0":
            tmp=l
            dp[r+l]=dp[r]+1
    r+=tmp
    #if r==n:break
    if tmp==0:
        print(-1)
        exit()
d = dp[-1]
rt = []
dp = dp[::-1]
r=0
while r<=n-1:
    l=0
    tmp=0
    while l+1<=m and r+l+1<=n:
        l+=1
        if dp[r+l]==d-1:
            tmp=l
    rt.append(tmp)
    d-=1
    r+=tmp
print(*reversed(rt))
