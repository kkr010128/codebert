import math
a, b = list(map(int, input().split()))
c = math.gcd(a, b)
d = a * b / c
d = math.floor(d)
print(d)