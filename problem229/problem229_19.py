import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    H, N, *AB = map(int, read().split())

    magic = [0] * N
    for i, (a, b) in enumerate(zip(*[iter(AB)] * 2)):
        magic[i] = (a, b)

    dp = [[INF] * (H + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 0

    for i in range(N):
        a, b = magic[i]
        for j in range(H + 1):
            dp[i + 1][j] = min(dp[i][j], dp[i + 1][max(j - a, 0)] + b)

    print(dp[N][H])
    return


if __name__ == '__main__':
    main()
