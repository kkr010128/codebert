def main():
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    INF = 10**10
    """
    使い回さない方
    dp = [[INF]*(N+1) for _ in range(M+1)]
    dp[0][0] = 0
    for i in range(M):
        for y in range(N+1):
            if C[i] > y:
                dp[i+1][y] = dp[i][y]
            else:
                dp[i+1][y] = min(dp[i][y], dp[i+1][y-C[i]]+1)
    print(min([dp[j][N] for j in range(1, M+1)]))
    """
    """ 使い回す方 """
    dp = [INF]*(N+1)
    dp[0] = 0
    for i in range(M):
        for y in range(N+1):
            if C[i] <= y:
                dp[y] = min(dp[y], dp[y-C[i]]+1)
    print(dp[N])


if __name__ == "__main__":
    main()
