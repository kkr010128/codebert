from math import gcd

x = int(input())
y = x * 360 // gcd(x, 360)
print(y//x)