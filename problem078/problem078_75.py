import math
n = int(input())
mod = 1000000007
all = pow(10, n, mod)
s1 = 2 * pow(9, n, mod) % mod
s2 = pow(8, n, mod) % mod
ans = int(all - s1 + s2)%mod
if ans < 0:
    ans += mod
print(ans%mod)