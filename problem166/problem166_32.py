def abc164_d():
    # 解説放送
    s = str(input())
    n = len(s)
    m = 2019
    srev = s[::-1]  # 下の位から先に見ていくために反転する
    x = 1  # 10^i ??
    total = 0  # 累積和 (mod 2019 における累積和)
    cnt = [0] * m  # cnt[k] : 累積和がkのものが何個あるか
    ans = 0
    for i in range(n):
        cnt[total] += 1
        total += int(srev[i]) * x
        total %= m
        ans += cnt[total]
        x = x*10 % m
    print(ans)

abc164_d()