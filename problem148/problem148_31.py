a, b, c, k = map(int, input().split())


if k - a <= 0:
    print(k)
elif k - a > 0 and k - a - b <= 0:
    print(a)
else:
    s = k - a - b
    print(a - s)
