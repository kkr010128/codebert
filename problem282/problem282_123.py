from operator import itemgetter
N, T = [int(i) for i in input().split()]

data = []
for i in range(N):
    data.append([int(i) for i in input().split()])

data.sort(key=itemgetter(0))

dp = [[0]*(T) for i in range(N)]
ans = data[0][1]
for i in range(1, N):
    for j in range(T):
        if j >= data[i-1][0]:
            value1 = dp[i-1][j]
            value2 = dp[i-1][j-data[i-1][0]] + data[i-1][1]
            dp[i][j] = max(value1, value2)
        else:
            dp[i][j] = dp[i-1][j]
    value3 = dp[i][T-1] + data[i][1]
    ans = max(value3, ans)
print(ans)
