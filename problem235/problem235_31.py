from fractions import gcd
def lcm(a, b):
    return a * b // gcd(a, b)

n = int(input())
a = list(map(int,input().split()))
mod = 10 ** 9 + 7

LCM = 1
a_mod = 0
for i in range(n):
    LCM = lcm(LCM, a[i])
    a_mod = (a_mod + pow(a[i], mod - 2, mod)) % mod

LCM = LCM % mod
ans = LCM * a_mod
print(ans % mod)