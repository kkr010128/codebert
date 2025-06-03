import math
a, b, c = map(int, input().split())
d = math.ceil(a / b)
print(d * c)