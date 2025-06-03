from collections import Counter
S = input()
L = len(list(S))
dp = [0] * L
dp[0] = 1
T = [0] * L
T[0] = int(S[-1])
for i in range(1, L):
    dp[i] =  dp[i - 1] * 10
    dp[i] %= 2019
    T[i] = int(S[-(i+1)]) * dp[i] + T[i - 1]
    T[i] %= 2019
ans = 0
for k, v in Counter(T).items():
    if k == 0:
        ans += v
        ans += v * (v - 1) // 2
    else:
        ans += v * (v - 1) // 2
print(ans)
