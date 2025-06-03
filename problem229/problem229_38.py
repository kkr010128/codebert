def main():
    h, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[float("inf")]*(2*10**4+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        p, a, b = i+1, arr[i][0], arr[i][1]
        for j in range(2*10**4+1):
            if j < a:
                dp[p][j] = dp[p-1][j]
            else:
                if dp[p][j-a] + b < dp[p-1][j]:
                    dp[p][j] = dp[p][j-a] + b
                else:
                    dp[p][j] = dp[p-1][j]
    print(min(dp[-1][h:2*10**4+1]))

if __name__ == "__main__":
    main()
