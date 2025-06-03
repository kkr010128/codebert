#E
H,N=map(int,input().split())
A=[0 for i in range(N)]
dp=[float("inf") for i in range(10**4+1)]
dp[0]=0
for i in range(N):
    a,b=map(int,input().split())
    A[i]=a
    for j in range(10**4+1):
        if j+a>10**4:
            break
        dp[j+a]=min(dp[j]+b,dp[j+a])


if H+max(A)>10**4:
    print(min(dp[H:]))
else:
    print(min(dp[H:H+max(A)]))