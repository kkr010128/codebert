import math

a,b,C = (int(x) for x in input().split())

S = a * b * math.sin(math.radians(C)) / 2
L = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(C))) + a + b
h = b * math.sin(math.radians(C))

print(round(S,8),round(L,8),round(h,8))
