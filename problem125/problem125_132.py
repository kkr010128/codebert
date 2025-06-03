from math import gcd

x = int(input())
lcm = 360 * x // gcd(360, x)
ans = lcm // x
print(ans)