n, T = map(int, input().split())
food = []
for _ in range(n):
    a, b = map(int, input().split())
    food.append((a, b))

dp1 = [[0]*T for _ in range(1+n)]
dp2 = [[0]*T for _ in range(1+n)]

for i in range(n):
    for j in range(T):
        dp1[i+1][j] = dp1[i][j]
        if j - food[i][0] >= 0:
            dp1[i+1][j] = max(dp1[i+1][j], dp1[i][j-food[i][0]] + food[i][1])

for i in range(n-1, -1, -1):
    for j in range(T):
        dp2[i][j] = dp2[i+1][j]
        if j - food[i][0] >= 0:
            dp2[i][j] = max(dp2[i][j], dp2[i+1][j-food[i][0]] + food[i][1])

res = 0
for i in range(n):
    for j in range(T):
        res = max(res, food[i][1] + dp1[i][j] + dp2[i+1][T-1-j])
print(res)