import sys

input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 9 + 7

H, N = map(int, input().split())
AB = [[] for _ in range(N)]
for i in range(N):
    AB[i] = list(map(int, input().split()))


def solve():

    dp = [INF] * (H + 1)
    dp[H] = 0

    for h in range(H, 0, -1):

        if dp[h] == INF:
            continue
        next_dp = dp

        for i in range(N):
            a, b = AB[i]
            hh = max(0, h - a)
            next_dp[hh] = min(dp[hh], dp[h] + b)

        dp = next_dp

    print(dp[0])


if __name__ == '__main__':
    solve()
