import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, t = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(n)]
    AB.sort()

    res = 0
    dp = [[0] * (t + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        a, b = AB[i - 1]
        for j in range(1, t + 1):
            if j - a >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a] + b)
            else:
                dp[i][j] = dp[i - 1][j]
        for k in range(i, n):
            _, b = AB[k]
            res = max(res, dp[i][j - 1] + b)
    print(res)


if __name__ == '__main__':
    resolve()
