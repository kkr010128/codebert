import math
a, b, C = map(int, input().split())
C = math.radians(C)
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C))
S = a * b * math.sin(C) / 2
print(f"{S:0.9f}")
print(f"{a+b+c:0.9f}")
print(f"{S*2/a:0.9f}")
