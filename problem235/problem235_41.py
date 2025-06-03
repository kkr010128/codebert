from fractions import gcd

n = int(input())
a = list(map(int, input().split()))
max_a = max(a)
mod = 10**9 + 7

inverse = [1] * (max_a + 1)
for i in range(2, max_a + 1):
  inverse[i] = -inverse[mod % i] * (mod // i) % mod

lcm = 1
for i in range(n):
  lcm = lcm * a[i] // gcd(lcm, a[i])
lcm %= mod

sum_b = 0
for i in range(n):
  sum_b = (sum_b + lcm * inverse[a[i]]) % mod
print(sum_b)