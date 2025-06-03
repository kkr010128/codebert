def main():
    from sys import stdin
    def input():
        return stdin.readline().strip()

    r, c, k = map(int, input().split())
    v = [[0] * c for _ in range(r)]
    for _ in range(k):
        i, j, k = map(int, input().split())
        v[i-1][j-1] = k

    # dp[j][n] = j列にいて、n個itemを拾った時のアイテムの価値の合計の最大値
    # 1行ずつdpを更新する
    # 0行目
    value = v[0][0]
    if value == 0:
        dp = [[0] * 4]
    else:
        dp = [[0, value, value, value]]
    for j in range(1, c):
        value = v[0][j]
        if value == 0:
            dp.append(dp[j-1])
            continue
        a = dp[j-1].copy()
        b = [0, a[0]+value, a[1]+value, a[2]+value]
        for k in range(1, 4):
            if a[k] < b[k]:
                a[k] = b[k]
        dp.append(a)

    # i行目
    for i in range(1, r):
        pre = dp[0][3]
        value = v[i][0]
        if value == 0:
            new_dp = [[pre] * 4]
        else:
            new_dp = [[pre, pre+value, pre+value, pre+value]]
        for j in range(1, c):
            value = v[i][j]
            if value == 0:
                a = new_dp[j-1].copy()
                b = [dp[j][3]] * 4
                for k in range(4):
                    if a[k] < b[k]:
                        a[k] = b[k]
                new_dp.append(a)
            else:
                a = new_dp[j-1].copy()
                pre = dp[j][3]
                b = [pre, pre+value, pre+value, pre+value]
                d = [a[0], a[0]+value, a[1]+value, a[2]+value]
                for k in range(4):
                    if a[k] < b[k]:
                        a[k] = b[k]
                    if a[k] < d[k]:
                        a[k] = d[k]
                new_dp.append(a)
        dp = new_dp

    print(dp[c-1][3])

main()