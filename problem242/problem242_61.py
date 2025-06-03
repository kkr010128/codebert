mod = 10 ** 9 + 7

n, k = map(int, input().split())
a = sorted(map(int, input().split()))

fact = [1] * n
inv = [1] * n
inv_fact = [1] * n

for i in range(2, n):
  fact[i] = fact[i-1] * i % mod
  inv[i] = -inv[mod % i] * (mod // i) % mod
  inv_fact[i] = inv_fact[i-1] * inv[i] % mod

max_sum = 0
for i in range(k-1, n):
  max_sum = (max_sum + a[i] * fact[i] * inv_fact[i-k+1]) % mod
max_sum = (max_sum * inv_fact[k-1]) % mod

min_sum = 0
for i in range(n-k+1):
  min_sum = (min_sum + a[i] * fact[n-i-1] * inv_fact[n-k-i]) % mod
min_sum = (min_sum * inv_fact[k-1]) % mod

print((max_sum - min_sum) % mod)