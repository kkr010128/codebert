import sys
from fractions import gcd
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
g = 0
lcm = 1
for x in a:
  g = gcd(lcm, x)
  lcm *= x // g
lcm %= mod
res = 0
for x in a:
  res += lcm * pow(x, mod - 2, mod) % mod
  res %= mod
print(res)