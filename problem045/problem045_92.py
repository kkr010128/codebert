import sys

[a, b] = [int(x) for x in sys.stdin.readline().split()]
d = a / b
r = a - a / b * b
f = round(1.0 * a / b, 7)

print d, r, f