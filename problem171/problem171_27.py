def main():
    # import sys
    # readline = sys.stdin.readline
    # readlines = sys.stdin.readlines
    N = int(input())
    A = [(a, i) for i, a in enumerate(map(int, input().split()))]
    A.sort(reverse=True)
    
    dp = [[-float('inf')] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for k in range(N):
        for i in range(k + 1):
            j = k - i
            here = dp[i][j]
            a, idx = A[k]
            dp[i + 1][j] = max(dp[i + 1][j], here + a * ((N - 1 - i) - idx))
            dp[i][j + 1] = max(dp[i][j + 1], here + a * (idx - j))
            # print(k, i)

    ans = 0
    for i in range(N + 1):
        j = N - i
        ans = max(ans, dp[i][j])
    print(ans)


if __name__ == "__main__":
    main()
