from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import sys
from fractions import gcd

for line in sys.stdin:
    small, large = sorted(int(n) for n in line .split())
    G = gcd(large, small)
    print(G, large // G * small)