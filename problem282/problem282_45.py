def main():
    N,T = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(N)]

    AB.sort()

    # dp[i][j]: 満足度の最大値
    # i: i品目まで
    # j: 制限時間(< T)
    dp = [[0] * 3100 for _ in range(3100)]

    dp[0][0] = 0

    # 貰うDP
    ans = 0
    for i in range(1, N + 1):
        for j in range(T):
            dp[i][j] = dp[i - 1][j]
            
            # ラストオーダーはAB[i - 1]
            ans = max(ans, dp[i][j] + AB[i - 1][1])

            if j - AB[i - 1][0] >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - AB[i - 1][0]] + AB[i - 1][1])

    print(ans)

if __name__ == "__main__":
    main()