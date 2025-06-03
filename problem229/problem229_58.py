a = list(map(int, input().split()))
HP = a[0]

x = []
for i in range(a[1]):
    x1, y1 = [int(i) for i in input().split()]
    x.append((x1, y1))

max_tup = max(x, key=lambda x: x[0]) #最高攻撃力の呪文を記憶
max_a = max_tup[0] #その攻撃力を記録
#1次元　横：与えるダメージ　中身：最小魔力
dp = [10**10] * (HP + max_a)  #DP表はHP+最高攻撃力
dp[0] = 0

for i in range(1, len(dp)):
    for a, b in x:
        if i >= a:
            dp[i] = min(dp[i],dp[i - a] + b )

print(min(dp[HP:]))