import math
(a, b, C) = [float(i) for i in input().split()]
S = 0.5 * a * b * math.sin(math.radians(C))
c = math.sqrt(a * a + b * b - 2 * a * b * math.cos(math.radians(C)))
print("%8f" %(S))
print("%8f" %(a + b + c))
print("%8f" %(S / a * 2))