import numpy as np
from itertools import permutations
N = int(input())

counter = np.zeros(N, dtype=int)

for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            res = x**2 + y**2 + z**2 + x * y + x * z + y * z
            if res <= N:  
                counter[res - 1] += 1

for c in counter:
    print(c)
