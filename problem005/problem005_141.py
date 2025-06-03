import sys

for line in sys.stdin:
    a, b = sorted(map(int, line.split(' ')))
    gcd = 1
    d = 2
    while a >= d:
        amod, bmod = a % d, b % d
        if amod == 0 and bmod == 0:
            gcd *= d
            a, b = a/d, b/d
            d = 2
            continue
        else:
            d += 1
    lcm = gcd * a * b
    print gcd, lcm