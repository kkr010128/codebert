import sys

for line in sys.stdin:
    n = [int(i) for i in line.replace("\n", "").split(" ")]
    n.sort()
    low = n[0]
    hi = n[1]
    while hi % low:
        hi, low = low, hi % low
    print("%d %d" % (low, n[0] / low * n[1]))