import math
a, b, c, d = map(float, input().split())
s1 = (a - c) * (a - c)
s2 = (b - d) * (b - d)
print("%.6f"%math.sqrt(s1+s2))

