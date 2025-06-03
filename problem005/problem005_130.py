import sys
for line in sys.stdin:
    a, b = map(int, line.split())
    A, B = min(a, b), max(a, b)

    while True:
        mod = B % A
        if mod == 0:
            gcd = A
            break
        else:
            A, B = mod, A
    lcm = gcd * (a / gcd) * (b / gcd)

    print '%d %d' % (gcd, lcm)