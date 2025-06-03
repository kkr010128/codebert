from math import ceil
from functools import reduce
print(reduce(lambda x, y: int(ceil(int(ceil(100000 * 1.05 / 1000) * 1000) * 1.05 / 1000) * 1000) if x == 0 else int(ceil(x * 1.05 / 1000) * 1000) , range(int(input()))))