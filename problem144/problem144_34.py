import math
a, b, h, m = map(int, input().split())

w_h = math.radians((h * 30) + (m * 0.5))
w_m = math.radians(m * 6)

x = (a ** 2) + (b ** 2) - (2 * a * b * math.cos(w_m - w_h))

print(math.sqrt(x))
