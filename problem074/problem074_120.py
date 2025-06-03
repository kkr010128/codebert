# 配るDP、もらうDP

n, k = map(int, input().split())
mod = 998244353

kukan = []
for _ in range(k):
    # 区間の問題は扱いやすいように[ )　の形に直せるなら直す
    l, r = map(int, input().split())
    l -= 1
    kukan.append([l, r])

dp = [0 for i in range(n)]
dp[0] = 1

# 区間のL, Rは数字が大きいため、その差一つ一つを考えると時間がない！
# それゆえにL, Rの端を考えればいいようにするためにそこまでの累和を考える
ruiseki = [0 for i in range(n + 1)]
ruiseki[1] = 1
for i in range(1, n):
    for l, r in kukan:
        l = i - l
        r = i - r
        l, r = r, l
        # print(l, r)
        if r < 0:
            continue
        elif l >= 0:
            dp[i] += (ruiseki[r] - ruiseki[l]) % mod
        else:
            dp[i] += (ruiseki[r]) % mod
    ruiseki[i + 1] = (ruiseki[i] + dp[i])
    # print(ruiseki, dp)

print(dp[-1] % mod)
