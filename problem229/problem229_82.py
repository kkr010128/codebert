
def resolve():
    INF = 1<<60
    H, N = map(int, input().split())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    dp = [INF]*(H+1)
    dp[0] = 0

    for h in range(H):
        for i in range(N):
            to = min(H, A[i]+h)
            dp[to] = min(dp[to], dp[h]+B[i])

    print(dp[H])


if __name__ == "__main__":
    resolve()
