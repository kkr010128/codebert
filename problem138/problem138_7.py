import pprint
N,S=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
dp=[[0 for _ in range(S+1)] for _ in range(N+1)]
dp[0][0]=1
#print(A)
p=998244353
for i in range(N):
    for j in range(S+1):
        dp[i+1][j]=(dp[i+1][j]+2*dp[i][j])%p
        if (j>=A[i]):
            dp[i+1][j]=(dp[i+1][j]+dp[i][j-A[i]])%p
print(dp[N][S])
