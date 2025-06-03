import math
a, b, x = map(int, input().split())
maxx = a * a * b
ans_rad = 0
if x + x <= maxx:
    c = 2 * x / (a * b)
    ans_rad = math.atan(b / c)
else:
    y = maxx - x
    c = 2 * y / (a * a)
    ans_rad = math.atan(c / a)

ans = math.degrees(ans_rad)
print(ans)