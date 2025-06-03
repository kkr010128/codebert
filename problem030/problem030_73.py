import math, re

a, b, c = [int(n) for n in re.split(r"\s+", input().strip())]
h = b * math.sin(c * math.pi / 180)
S = a * h / 2
L = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(c * math.pi / 180)) + a + b
print("%f %f %f" % (S, L, h))

