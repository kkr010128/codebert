import math

a, b, h, m = map(int, input().split())
ang_a = (360 * h / 12) + (0.5 * m)
ang_b = 360 * m / 60
ang = abs(ang_a - ang_b)

ans = math.sqrt((a ** 2 + b ** 2) - (2*a*b*math.cos(math.radians(ang))))
print(ans)
