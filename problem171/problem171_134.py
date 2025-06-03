import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(input())
    a = list(map(int, readline().split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        val = max(a)
        idx = a.index(val)
        a[idx] = 0
        for j in range(i + 1):
            left = j
            right = i - j
            prev = dp[left][right]
            dp[left + 1][right] = max(dp[left + 1][right], prev + val * (idx - left))
            dp[left][right + 1] = max(dp[left][right + 1], prev + val * ((n - 1 - right) - idx))

    ans = 0
    for i in range(n):
        ans = max(ans, dp[i][n - i])

    print(ans)


if __name__ == '__main__':
    main()
