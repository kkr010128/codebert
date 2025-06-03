INF = 100 ** 7


def main():
    n, m = map(int, input().split())
    c_list = list(map(int, input().split()))

    dp = [INF] * (n + 1)
    dp[0] = 0
    for c in c_list:
        for i in range(len(dp)):
            if dp[i] != INF and i + c < len(dp):
                dp[i + c] = min(dp[i + c], dp[i] + 1)
    print(dp[n])


if __name__ == '__main__':
    main()