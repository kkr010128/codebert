import sys
from copy import copy
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')

INF = 10**9 + 7


def main():
    H, W = in_nn()
    s = [list(in_s()) for _ in range(H)]

    dp = [INF] * W
    if s[0][0] == '#':
        dp[0] = 1
    else:
        dp[0] = 0

    for x in range(W - 1):
        if s[0][x] == '.' and s[0][x + 1] == '#':
            dp[x + 1] = dp[x] + 1
        else:
            dp[x + 1] = dp[x]

    for y in range(1, H):
        next_dp = [INF] * W
        for x in range(W):
            if s[y - 1][x] == '.' and s[y][x] == '#':
                next_dp[x] = min(next_dp[x], dp[x] + 1)
            else:
                next_dp[x] = min(next_dp[x], dp[x])
        for x in range(1, W):
            if s[y][x - 1] == '.' and s[y][x] == '#':
                next_dp[x] = min(next_dp[x], next_dp[x - 1] + 1)
            else:
                next_dp[x] = min(next_dp[x], next_dp[x - 1])

        dp = next_dp

    print(dp[-1])


if __name__ == '__main__':
    main()
