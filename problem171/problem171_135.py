N=int(input())
A=list(map(int,input().split()))
B=[]
for k in range(N):
    B.append([A[k],k+1])
B.sort(key=lambda x: x[0], reverse=True)
dp=[[0 for k in range(N+1)]for k in range(N+1)]
dp[1][0]=dp[0][0]+B[0][0]*(B[0][1]-1)
dp[0][1]=dp[0][0]+B[0][0]*(N-B[0][1])
for k in range(1,N):
    #j=0
    dp[0][k+1]=dp[0][k]+B[k][0]*(N-k-B[k][1])
    dp[1][k]=max(dp[0][k]+B[k][0]*(B[k][1]-1), dp[1][k-1]+B[k][0]*(N-k+1-B[k][1]))
    #j=k
    dp[k+1][0]=dp[k][0]+B[k][0]*(B[k][1]-k-1)
    dp[k][1]=max(dp[k-1][+1]+B[k][0]*(B[k][1]-k), dp[k][0]+B[k][0]*(N-B[k][1]))
    for j in range(1,k):
        dp[j+1][k-j]=max(dp[j][k-j]+B[k][0]*(B[k][1]-j-1), dp[j+1][k-j-1]+B[k][0]*(N-k+j+1-B[k][1]))
        dp[j][k-j+1]=max(dp[j-1][k-j+1]+B[k][0]*(B[k][1]-j), dp[j][k-j]+B[k][0]*(N-k+j-B[k][1]))
ans=[]
for k in range(N+1):
    ans.append(dp[k][N-k])
print(max(ans))               