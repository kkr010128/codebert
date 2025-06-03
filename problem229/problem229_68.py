import sys

read = sys.stdin.buffer.read
INF = 1 << 60


def main():
    H, N, *AB = map(int, read().split())

    dp = [INF] * (H + 1)
    dp[0] = 0

    for a, b in zip(*[iter(AB)] * 2):
        for i in range(H + 1):
            if dp[i] > dp[max(i - a, 0)] + b:
                dp[i] = dp[max(i - a, 0)] + b

    print(dp[H])
    return


if __name__ == '__main__':
    main()
