import math
a,b,c = map(float, input().split())
cc = math.radians(c)
h = b * math.sin(cc)
S = a * h / 2
L = a + b + math.sqrt(h**2 + (a-b*math.cos(cc))**2)
print("{0:.10f}\n{1:.10f}\n{2:.10f}\n".format(S, L, h))