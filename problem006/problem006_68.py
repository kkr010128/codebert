import sys, math

for line in sys.stdin.readlines():
    line = line.strip()
    n = int(line)
    value = 100000.0
    for week in xrange(n):
        value = value * 1.05
        value = math.ceil(value / 1000) * 1000
    print int(value)