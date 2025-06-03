
import sys
MOD = 998244353


def main():
    input = sys.stdin.buffer.readline
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[None] * (s + 1) for _ in range(n + 1)]
#     dp[i][j]:=集合{1..i}の空でない部分集合T全てについて,和がjとなる部分集合の個数の和
    for i in range(n + 1):
        for j in range(s + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
                continue
            if j > a[i - 1]:
                dp[i][j] = dp[i - 1][j] * 2 + dp[i - 1][j - a[i - 1]]
            elif j == a[i - 1]:
                dp[i][j] = dp[i - 1][j] * 2 + pow(2, i - 1, MOD)
            else:
                dp[i][j] = dp[i - 1][j] * 2
            dp[i][j] %= MOD
    print(dp[n][s])


if __name__ == '__main__':
    main()
