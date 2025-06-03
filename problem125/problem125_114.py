import math
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
x = int(input())
lcm = lcm_base(360, x)
print(lcm//x)