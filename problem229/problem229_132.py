import sys


def main():
    input = sys.stdin.buffer.readline
    h, n = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    max_a = max(a)
    # dp[j]:jダメージ与える魔力の最小値
    dp = [1e9] * (h + max_a + 1)
    dp[0] = 0
    for i in range(n):
        for j in range(1, h + max_a + 1):
            dp[j] = min(dp[j], dp[max(j - a[i], 0)] + b[i])
    print(min(dp[h:]))


if __name__ == "__main__":
    main()
