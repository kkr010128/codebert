N=int(input())
A=[int(a) for a in input().split()]
dp=[-1 for _ in range(N)]
dp[0]=1000
for i in range(1,N):
    tmp=dp[i-1]
    for j in range(i):
        K=dp[j]//A[j]
        res=dp[j]-K*A[j]
        tmp=max(tmp,res+A[i]*K)
    dp[i]=tmp
print(dp[-1])