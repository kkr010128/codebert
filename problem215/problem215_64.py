mod = 10 ** 9 + 7
n, k = map(int, input().split())

fact = [1] * (2 * n + 1)
inv = [1] * (2 * n + 1)
invf = [1] * (2 * n + 1)
for i in range(2, 2 * n + 1):
  fact[i] = fact[i-1] * i % mod
  inv[i] = -inv[mod % i] * (mod // i) % mod
  invf[i] = invf[i-1] * inv[i] % mod

count = 0
for i in range(min(n, k+1)):
  c = fact[n] * invf[n-i] * invf[i] % mod
  count += c * fact[n-1] * invf[n-i-1] * invf[i] % mod
  count %= mod
print(count)