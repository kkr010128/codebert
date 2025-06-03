from copy import deepcopy

# 多次元配列を作成する
def make_multi_list(initial, degree):
    ans = [initial for _ in range(degree[-1])]
    for d in reversed(degree[:-1]):
        ans = [deepcopy(ans) for _ in range(d)]
    return ans


N, T = map(int, input().split())
AB = []
for i in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))
AB.sort()

ans = 0
dp = make_multi_list(0, [3005, 3005])
for i in range(N):
    a, b = AB[i]
    for j in range(T):
        # iを使わないパターン
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        # iを使うパターン
        nj = j + a
        if nj < T:
            dp[i + 1][nj] = max(dp[i + 1][nj], dp[i][j] + b)
    now = dp[i][T - 1] + b
    ans = max(ans, now)

print(ans)
