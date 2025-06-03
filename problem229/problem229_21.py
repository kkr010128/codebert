import sys

read = sys.stdin.read
INF = 1 << 60


def main():
    H, N, *AB = map(int, read().split())

    dp = [INF] * (H + 1)
    dp[0] = 0

    for a, b in zip(*[iter(AB)] * 2):
        for i in range(H + 1):
            if i >= a:
                if dp[i] > dp[i - a] + b:
                    dp[i] = dp[i - a] + b
            else:
                if dp[i] > dp[0] + b:
                    dp[i] = dp[0] + b

    print(dp[H])
    return


if __name__ == '__main__':
    main()
