import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    R, C, K = map(int, input().split())

    field = [[0 for j in range(C)] for i in range(R)]

    for _ in range(K):
        r, c, v = map(int, input().split())
        field[r - 1][c - 1] = v

    dp = [[[0] * C for j in range(R)] for i in range(4)]

    for i in range(R):
        for j in range(C):
            ct = field[i ][j ]
            pm = max(dp[0][i-1][j],dp[1][i-1][j],dp[2][i-1][j],dp[3][i-1][j])
            if ct == 0:
                dp[0][i][j] = max(dp[0][i][j-1],pm)

                for k in range(1, 4):
                    if j>0:
                        dp[k][i][j] = dp[k][i][j - 1]
            else:
                dp[0][i][j] = max(dp[0][i][j - 1],pm)
                dp[1][i][j] = max(ct + max(dp[0][i][j - 1], pm),dp[1][i][j-1])
                for k in range(2, 4):
                    if j >0:
                        dp[k][i][j] = max(dp[k - 1][i][j - 1] +ct,dp[k][i][j-1])

    print(max(dp[0][R-1][C-1],dp[1][R-1][C-1],dp[2][R-1][C-1],dp[3][R-1][C-1]))

if __name__ == "__main__":
    main()
