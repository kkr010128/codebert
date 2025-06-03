def main():
    N, T = list(map(int, input().split(' ')))
    foods = [list(map(int, input().split(' '))) for _ in range(N)]
    # 食べ物は食べる時間の昇順に並べ替え、短い方を優先して食べるようにしておく。
    foods.sort(key=lambda food: food[0])
    # dp[n][t]: n個目までの食べ物のうち、時刻tまでに食べきる場合に得られるおいしさの合計の最大値。
    dp = [[0 for _ in range(T + 1)] for _ in range(N + 1)]
    for i, food in enumerate(foods):
        n = i + 1
        A, B = food
        for t in range(T + 1):
            val = dp[n - 1][t]
            if t - A >= 0 and dp[n - 1][t - A] + B > val:
                val = dp[n - 1][t - A] + B
            dp[n][t] = val
    # これを求める
    # max_n {dp[n - 1][T - 1] + (n個目の食べ物のおいしさ)}
    ans = 0
    for n in range(1, N + 1):
        v = dp[n - 1][T - 1] + foods[n - 1][1]
        ans = max(ans, v)
    print(ans)


if __name__ == '__main__':
    main()
