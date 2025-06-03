import sys, fractions
[[print("{} {}".format(int(fractions.gcd(t[0], t[1])), int(t[0] * t[1] / fractions.gcd(t[0], t[1])))) for t in [[int(y) for y in x.split()]]] for x in sys.stdin]