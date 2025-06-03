import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    R, C, K = map(int, input().split())

    field = [[0 for j in range(C)] for i in range(R)]

    for _ in range(K):
        r, c, v = map(int, input().split())
        field[r - 1][c - 1] += v

    #    dp = [[0] * 4 for j in range(C)]
    dp0 = [0] * C
    dp1 = [0] * C
    dp2 = [0] * C
    dp3 = [0] * C

    for i in range(R):
        for j in range(C):
            ct = field[i][j]
            premax = max(dp0[j], dp1[j], dp2[j], dp3[j])

            if ct == 0:
                if j > 0:
                    dp0[j] = max(dp0[j - 1], premax)
                    dp1[j] = dp1[j - 1]
                    dp2[j] = dp2[j - 1]
                    dp3[j] = dp3[j - 1]
                else:
                    dp0[j] = premax

                # for k in range(1, 4):
                #     if j > 0:
                #         dp[j][k] = dp[j - 1][k]
                #




            # else:
            #     if j > 0:
            #         dp[j][0] = max(dp[j - 1][0], premax)
            #         dp[j][1] = max(ct + max(dp[j - 1][0], premax), dp[j - 1][1])
            #     else:
            #         dp[j][0] = premax
            #         dp[j][1] = premax + ct
            #     for k in range(2, 4):
            #         if j > 0:
            #             dp[j][k] = max(dp[j - 1][k - 1] + ct, dp[j - 1][k])
            else:
                if j > 0:
                    dp0[j] = max(dp0[j - 1], premax)
                    dp1[j] = max(ct + max(dp0[j - 1], premax), dp1[j - 1])
                    dp2[j] = max(dp1[j - 1] + ct, dp2[j - 1])
                    dp3[j] = max(dp2[j - 1] + ct, dp3[j - 1])
                else:
                    dp0[j] =premax
                    dp1[j] = premax+ct

    #print(max(dp[C - 1]))
    print(max(dp0[C-1], dp1[C-1], dp2[C-1], dp3[C-1]))

if __name__ == "__main__":
    main()
