import math
a, b, x = map(float, input().split())
vol = a * a * b
if x <= vol/2:
    height = (x * 2.0) / (b * a)
    ans = math.atan(b / height) * 180 / math.pi
else:
    height = ((vol - x) * 2.0) / (a * a)
    ans = math.atan(height / a) * 180 / math.pi
print(ans)