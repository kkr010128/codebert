import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, T, *AB = map(int, read().split())
    D = [(a, b) for a, b in zip(*[iter(AB)] * 2)]

    D.sort()

    dp = [[0] * T for _ in range(N + 1)]
    for i, (a, b) in enumerate(D):
        for t in range(T):
            if 0 <= t - a:
                dp[i + 1][t] = dp[i][t - a] + b
            if dp[i + 1][t] < dp[i][t]:
                dp[i + 1][t] = dp[i][t]

    ans = 0
    for i in range(N - 1):
        if ans < dp[i + 1][T - 1] + D[i + 1][1]:
            ans = dp[i + 1][T - 1] + D[i + 1][1]

    print(ans)
    return


if __name__ == '__main__':
    main()
