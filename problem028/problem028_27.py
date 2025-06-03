import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    C = list(map(int, input().split()))

    dp = [f_inf] * (n + 1)
    dp[0] = 0
    for c in C:
        for i in range(1, n + 1):
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i - c] + 1)
    print(dp[-1])


if __name__ == '__main__':
    resolve()

