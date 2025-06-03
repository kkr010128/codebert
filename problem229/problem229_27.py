INF=10**30
H,N=map(int,input().split())
A,B=[],[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a);B.append(b)
dp=[INF]*(H+10)
dp[0]=0
for i in range(N):
    for j in range(H+1):
        if(j<A[i]):
            dp[j]=min(dp[j],dp[0]+B[i])
        else:
            dp[j]=min(dp[j],dp[j-A[i]]+B[i])
print(dp[H])