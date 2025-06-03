import math
a, b, x = map(int, input().split())

# 水が多いか少ないかで作図が変わってくる

# 半分以上水が入っている場合
if x >= a**2 * b / 2:
    # 限界の時、a**2 * b - 0.5 * a**2 * tanθ * a = x
    tan = 2 * (a**2 * b - x) / a**3
    ans = math.degrees(math.atan(tan))
    print(ans)

# 半分以下の場合
else:
    # 限界の時、0.5 * b**2 * tan(90 - θ) * a = x
    # tan(90 - θ) = 1/tanθ
    tan = (a * b**2) / (2 * x)
    ans = math.degrees(math.atan(tan))
    print(ans)
