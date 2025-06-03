import math
base = 100000
r = 0.05
n = int(raw_input())
if n <= 100:
    for i in range(1, n+1):
        base = base + (base * r)
        now = int(math.ceil(base / 1000))
        base = now * 1000
    print "{}".format(base)