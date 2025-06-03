INF = 10 ** 7
N,T = map(int,input().split())
foods = []
for _ in range(N):
    foods.append(list(map(int,input().split())))

foods.sort()
dp = [[-INF for i in range(T)] for j in range(N+1)]
dp[0][0] = 0
ans = 0

for i in range(N):
    food = foods[i]
    for j in range(T):
        ans = max(ans, dp[i][j] + food[1])
        if dp[i][j] != INF:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j + food[0] < T:
                dp[i+1][j + food[0]] = max(dp[i+1][j + food[0]], dp[i][j] + food[1])

print(ans)