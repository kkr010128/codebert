import math

(a,b,C) = [int(i) for i in input().split()]

c = math.sqrt(a ** 2 + b ** 2 - (2 * a * b) * math.cos(C * math.pi / 180))
h = float(b * math.sin(C * math.pi / 180))
s = float(a * h / 2)
l = float(a + b + c)

print(s)
print(l)
print(h)