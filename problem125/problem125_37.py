import math
x = int(input())

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

print(lcm(x, 360)//x)
