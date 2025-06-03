import math

N = int(input())
A = list(map(int, input().split()))

mod = 10**9+7

primes = [0]*(10**6+1)

def prime_fac(n):
  temp = n
  Flag = True
  for i in range(2, int(math.sqrt(n)) + 1):
    if temp % i == 0:
      cnt = 0
      while temp % i == 0:
        cnt += 1
        temp //= i
      primes[i] = max(primes[i], cnt)
      Flag = False
  if temp != 1:
    primes[temp] = max(primes[temp], 1)
  if Flag:
    primes[n] = max(primes[n], 1)

for a in A:
  prime_fac(a)

LCM = 1
for p, i in enumerate(primes):
  if i:
    LCM *= pow(p, i, mod)
    LCM %= mod

ans = 0
for a in A:
  ans += LCM * pow(a, mod-2, mod) % mod
  ans %= mod

print(ans)