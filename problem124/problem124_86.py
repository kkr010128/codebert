K = int(input())
S = input()
MOD = 10**9 + 7

length = len(S)
length_all = K + length
ans = 0
list_25 = [1] * (10**6 + 5)
list_26 = [1] * (10**6 + 5)
for i in range(1,10**6 + 5):
  list_25[i] = list_25[i - 1] * 25 % MOD
  list_26[i] = list_26[i - 1] * 26 % MOD
  
fact = [1] * (2 * 10**6 + 5)
fact_inv = [1] * (2 * 10**6 + 5)
for i in range(1, 2 * 10**6 + 5):
  fact[i] = fact[i-1] * i % MOD
  fact_inv[i] = fact_inv[i - 1] * pow(i, MOD - 2, MOD) % MOD

for i in range(K + 1):
  ans += list_26[i] * list_25[K - i] % MOD * fact[length_all - i - 1] * fact_inv[length - 1] * fact_inv[K - i] % MOD

print(ans % MOD)