import math
a, b, k = list(map(int, input().split(' ')))
if k > a*a*b / 2:
    # k = a*a*b - a*a*p/2 | pは斜めの水の内側の高さの方の辺, p = b で丁度半分
    # p = 2b - 2k/(a*a)
    p = 2*b - 2*k / (a*a)
    # 三角形の長い方をqとして qq = pp + aa
    q = (p**2 +a**2) ** 0.5
    
    # q * sin(r) = p
    # r = ... わからんので 2分探索
    left = 0.0
    right = 90.0
    while right > left + 1e-12:
        r = (left + right) / 2.0
        if q * math.sin(math.radians(r)) < p:
            left = r
        else:
            right = r
else:
    # k = a*b*p/2
    # p = 2*k/(a*a)
    p = 2*k/(a*b)
    # 三角形の長い方をqとして qq = pp + aa
    q = (p**2 +b**2) ** 0.5
    # r = ... わからんので 2分探索
    left = 0.0
    right = 90.0
    while right > left + 1e-12:
        r = (left + right) / 2.0
        if q * math.sin(math.radians(r)) < b:
            left = r
        else:
            right = r
print(r)