
def resolve():
    N, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    dp = [[0] * (T + 1) for _ in range(N + 1)]

    for i in range(N):
        t, v = AB[i]
        for j in range(T + 1):
            if t + j <= T:
                dp[i + 1][j + t] = max(dp[i + 1][j + t], dp[i][j] + v)
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

    ans = 0
    for i, (t, v) in enumerate(AB):
        ans = max(ans, dp[i][T - 1] + v)
    print(ans)


if __name__ == "__main__":
    resolve()
