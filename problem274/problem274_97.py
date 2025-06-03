# -*- coding: utf-8 -*-
n,m = list(map(int,input().split()))
s = input()


inf=float("inf")
#i番目のマスに行くための最小手数と、なんマス移動してきたか
dp = [(0,0)] + [(inf,None) for _ in range(n)]
for i in range(1,n+1):
    if s[i]=="0":
        for j in range(min(m,i),0,-1):
            if dp[i-j][0]<inf:
                dp[i]=(dp[i-j][0]+1,j)
                break
if dp[-1][1]:
    i = n
    ret = []
    ra = ret.append
    while dp[i][1]:
        ra(dp[i][1])
        i-=dp[i][1]
    print(" ".join(map(str,ret[::-1])))
else:
    print(-1)