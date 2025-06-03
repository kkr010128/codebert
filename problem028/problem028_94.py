import sys


def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    c = [0] + list(map(int, input().split()))
    dp = [list(range(n + 1)) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(n + 1):
            if j - c[i] >= 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - c[i]] + 1)
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[m][n])


if __name__ == "__main__":
    main()

