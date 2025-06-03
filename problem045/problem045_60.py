a, b = map(int, input().split())

if (a >= 1 and a <= 1000000000) and (b >= 1 and b <= 1000000000):
    d = int(a / b)
    r = int(a % b)
    f = float(a / b)

    print("{0:d} {1:d} {2:f}".format(d, r, f))
else:
    pass