import math

a,b,c = [float(s) for s in input().split()]
r = c * math.pi / 180
h = math.sin(r) * b
s = a * h / 2

x1 = a
y1 = 0
if c == 90:
    x2 = 0
else:
    x2 = math.cos(r) * b
y2 = h

d = math.sqrt((math.fabs(x1 - x2) ** 2) + (math.fabs(y1 - y2) ** 2))
l = a + b + d

print(s)
print(l)
print(h)