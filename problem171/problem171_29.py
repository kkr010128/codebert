def main():
    from operator import itemgetter

    N = int(input())
    a = map(int, input().split())

    *ea, = enumerate(a, 1)

    ea.sort(key=itemgetter(1), reverse=True)

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    # dp[left][right]:=活発な幼児から順に左端からleft,右端からright並べた際の最大うれしさ

    for i, (p, x) in enumerate(ea, 1):
        for left in range(i + 1):
            right = i - left
            if left > 0:
                dp[left][right] = max(
                    dp[left][right],
                    dp[left - 1][right] + x * (p - left)
                )
            if right > 0:
                dp[left][right] = max(
                    dp[left][right],
                    dp[left][right - 1] + x * (N - right + 1 - p)
                )

    ans = max(dp[i][N - i] for i in range(N + 1))
    print(ans)


if __name__ == '__main__':
    main()
