import math

N = int(input())
A = list(map(int, input().split()))

mod = 10**9+7

def lcm(x, y):
  return (x // math.gcd(x, y)) * y

LCM = A[0]
for i in range(N-1):
  LCM = lcm(LCM, A[i+1])

#LCM %= mod

ans = 0
for a in A:
  ans += LCM * pow(a, mod-2, mod) % mod
  ans %= mod

print(ans)