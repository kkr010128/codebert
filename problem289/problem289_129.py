import math

a, b, x = map(int, input().split(' '))

base = a * a * b /2

if int(base) == x:
    print(math.degrees(math.atan(b/a)))
elif base > x:
    ah = 2 * x / (a * b)
    print(math.degrees(math.atan(b/ah)))
else:
    bh = 2 * x / a ** 2 - b
    c = b - bh
    print(math.degrees(math.atan(c/a)))
