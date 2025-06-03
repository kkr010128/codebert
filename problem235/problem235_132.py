import sys
from fractions import gcd

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 10 ** 9 + 7
N = ir()
A = lr()
lcm = 1
answer = 0
for a in A:
    coef =  a // gcd(lcm, a)
    answer *= coef
    lcm *= coef
    answer += lcm // a

print(answer%MOD)
