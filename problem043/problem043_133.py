import sys
for d in sys.stdin:
    x, y = map(int, d.split())
    if (x, y) == (0, 0): break
    print("{0} {1}".format(min(x, y), max(x, y)))