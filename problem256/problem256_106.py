import math

from numpy.compat.py3k import asstr
a, b = map(int, input().split())
ans = int(a * b / math.gcd(a, b))
print(str(ans))
