import sys
input = sys.stdin.readline
I=lambda:int(input())
MI=lambda:map(int,input().split())
LI=lambda:list(map(int,input().split()))

N,T=MI()
dp=[[0]*(T+1) for _ in [0]*(N+1)]
food=[tuple(MI()) for _ in [0]*N]
food.sort()

for n in range(N):
    a,b=food[n]
    for t in range(T+1):
        if t<T:
            # たべる
            dp[n+1][min(t+a,T)]=max(dp[n][t]+b,dp[n+1][min(t+a,T)])
        # たべない
        dp[n+1][t]=max(dp[n][t],dp[n+1][t])
print(dp[N][T])