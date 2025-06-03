import sys
import math

r, c = map(int, raw_input().split())
b = [0 for i in xrange(c+1)]

for i in xrange(r):
    a = map(int, raw_input().split())

    for j in xrange(c):
        b[j] += a[j]
        sys.stdout.write(str(a[j]) + " ")
    print sum(a)

    b[c] += sum(a)

for j in xrange(c+1):
    sys.stdout.write(str(b[j]))
    if j < c:
        sys.stdout.write(" ")
print