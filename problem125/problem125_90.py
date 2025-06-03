import math

x = int(input())
if 360 % x == 0:
    print(360 // x)
else:
    common = 360 * x // math.gcd(360, x)
    ans = common // x
    print(ans)
