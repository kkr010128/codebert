from math import gcd
from itertools import product
from functools import reduce

l1 = [i for i in range(1, int(input()) + 1)]
print(sum(reduce(gcd, l) for l in product(l1, repeat=3)))