import math

x = int(input())

z = (x * 360) // math.gcd(x, 360)

print(z//x)