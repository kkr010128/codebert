import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
mod = 10**9+7

import fractions
lc = num[0]
for i in range(1, n):
    lc = lc * num[i] // fractions.gcd(lc, num[i])

lc %= mod    
def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

ans =0
for i in range(n):
  ans += lc*modinv(num[i],mod)
  ans %= mod
print(ans)