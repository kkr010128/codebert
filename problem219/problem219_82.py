# E - Payment

S = input()
N = len(S)

# 先頭からi桁目までの金額のやり取りに必要な紙幣の枚数
dp = [0]
dp_plus1 = [1]

for i in range(N):
    x = int(S[i])
    dp.append(min(dp[i] + x, dp_plus1[i] + (10 - x)))
    dp_plus1.append(min(dp[i] +  (x + 1), dp_plus1[i] + (10 -  (x + 1))))

print(dp[-1])