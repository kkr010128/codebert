#E
N,T=map(int,input().split())
A=[0 for i in range(N+1)]
B=[0 for i in range(N+1)]
for i in range(1,N+1):
    A[i],B[i]=map(int,input().split())

dp1=[[0 for i in range(6001)] for j in range(N+1)]
dp2=[[0 for i in range(6001)] for j in range(N+2)]

for i in range(1,N+1):
    for j in range(T+1):
        if j>=A[i]:
            dp1[i][j]=max(dp1[i-1][j],dp1[i-1][j-A[i]]+B[i])
        else:
            dp1[i][j]=dp1[i-1][j]

for i in range(N,0,-1):
    for j in range(T+1):
        if j>=A[i]:
            dp2[i][j]=max(dp2[i+1][j],dp2[i+1][j-A[i]]+B[i])
        else:
            dp2[i][j]=dp2[i+1][j]

ans=0
for i in range(1,N+1):
    for j in range(T):
        ans=max(ans,dp1[i-1][j]+dp2[i+1][T-1-j]+B[i])
print(ans)