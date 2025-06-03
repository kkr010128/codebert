import sys

N = int(raw_input())
for line in sys.stdin:
    a, b, c = sorted(map(int, line.split()))
    if a ** 2 + b ** 2 == c ** 2:
        print 'YES'
    else:
        print 'NO'