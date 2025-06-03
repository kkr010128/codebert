import math
a, b, c = [float(i) for i in input().split()]
print(a * b * math.sin(math.radians(c)) / 2)
print(a + b + math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(c))))
print(b * math.sin(math.radians(c)))