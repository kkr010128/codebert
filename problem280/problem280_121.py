import numpy as np
from itertools import combinations
from itertools import permutations
from math import factorial


N = int(input())
xy = np.array([list(map(int, input().split())) for _ in range(N)])
cnt = 0

for i in xy:
    for j in xy:
        cnt += np.linalg.norm(i - j)
print(cnt / N)