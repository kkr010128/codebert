import sys

MOD = 10**9+7
s = int(input())

dp = [0, 0, 0, 1]
ruisekiwa = [0, 0, 0, 0]

if s < 3:
    print(0)
    sys.exit()

for i in range(4, s+1):
    dp.append(1 + ruisekiwa[i-1])
    ruisekiwa.append(dp[i-2] + ruisekiwa[i-1])

# print(dp)
# print(ruisekiwa)
print(dp[-1] % MOD)
