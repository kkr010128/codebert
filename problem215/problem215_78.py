n, k = map(int, input().split())
MOD = 10**9 + 7

fact = [0] * (n+1)
inv_fact = [0] * (n+1)

fact[0] = 1
for i in range(1, n+1):
    fact[i] = fact[i-1] * i % MOD

inv_fact[n] = pow(fact[n], MOD-2, MOD)
for i in range(n, 0, -1):
    inv_fact[i-1] = inv_fact[i] * i % MOD


def nCk(n, k):
    return fact[n] * inv_fact[k] * inv_fact[n-k] % MOD
  
ans = 1
for i in range(1, n):
    if i > k:
      break
    ans += nCk(n, i) * nCk(n-1, n-i-1) % MOD
print(ans % MOD)