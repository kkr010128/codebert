import math

a, b, h, m = map(int, input().split())
rad_a = 2 * math.pi / 720 * (60 * h + m)
rad_b = 2 * math.pi / 60 * m

ans = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(rad_a - rad_b))
print("{:.20f}".format(ans))