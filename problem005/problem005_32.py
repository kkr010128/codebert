import sys
from fractions import gcd
for line in sys.stdin:
    a, b = map(int, line.split())
    print gcd(a, b), a*b/gcd(a,b)