import math

a, b, h, m = map(int,input().split())

time = h * 60 + m

ta = time * 2 * math.pi / (12 * 60)
tb = time * 2 * math.pi / 60

xa = a * math.sin(ta)
ya = a * math.cos(ta)
xb = b * math.sin(tb)
yb = b * math.cos(tb)

ans = math.sqrt((xa-xb)**2 + (ya-yb)**2)
print(ans)