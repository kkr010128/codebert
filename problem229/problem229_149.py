H,N = map(int,input().split())

AB = [list(map(int,input().split())) for _ in range(N)]

dp = [[10000000000000]*(H+1) for _ in range(N+1)]

for y in range(N):
    a,b = AB[y]
    for x in range(H+1):
        if x <= a:
            dp[y+1][x] = min(dp[y][x], b)
        else:
            dp[y+1][x] = min(dp[y][x], dp[y+1][x-a]+b)
print(dp[-1][-1])