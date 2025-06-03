from math import atan, pi

a, b, x = map(int, input().split())
if a * a * b > 2 * x:
    ans = atan(a * b * b / 2 / x)
else:
    ans = atan((2 * a * a * b - 2 * x) / a / a / a)

ans *= 180 / pi
print(ans)
