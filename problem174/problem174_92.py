import sys
import itertools
from math import gcd

n = int(sys.stdin.read())
print(sum(gcd(gcd(abc[0], abc[1]), abc[2]) for abc in itertools.product(range(1, n + 1), repeat=3)))
