import numpy as np
N = int(input())
L = np.array(input().split(),dtype = int)

m = min(N,max(L))

r = np.array(np.linspace(1,m,m),int)


dp = [0 for i in range(N+1)]

for i in range(0,N):
    if dp[i]+1 ==L[i]:
        dp[i+1] = dp[i]+1
    else:
        dp[i+1] = dp[i]

a = max(dp)
if a == 0:
    print(-1)
else:
    print(N-a)