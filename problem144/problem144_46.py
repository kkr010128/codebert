import math

a, b, h, m = map(int, input().split())

rad1 = (2 * math.pi) * ((h * 60 + m) / 720)
rad2 = (2 * math.pi) * (m / 60)
x = abs(rad2 - rad1)
ans = math.sqrt(a * a + b * b - 2 * a * b * math.cos(x))
print(ans)