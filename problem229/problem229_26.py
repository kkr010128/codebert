def main():
    INF = 10 ** 10
    H, N = list(map(int, input().split(' ')))
    magic = [list(map(int, input().split(' '))) for _ in range(N)]
    MAX_A = max(list(map(lambda x: x[0], magic)))
    dp = [INF for _ in range(MAX_A + H + 1)]
    dp[0] = 0
    for h in range(1, MAX_A + H + 1):
        for i in range(N):
            a, b = magic[i]
            if h - a < 0:
                continue
            dp[h] = min(dp[h], b + dp[h - a])
    print(min(dp[H:]))


if __name__ == '__main__':
    main()