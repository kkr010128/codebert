import math

n, x, t = map(int, input().split())

c = math.floor(n / x)

if n % x == 0:
    print(c * t)
else:
    print(c * t + t)