import sys
from fractions import gcd
[print("{} {}".format(gcd(*x), x[0] * x[1] // gcd(*x))) for x in [list(map(int, x.split())) for x in sys.stdin]]