import numpy as np
MOD = 10 ** 9 + 7
N = int(input())
A = np.array(input().split(), dtype=np.int64)
total = 0
for shamt in range(65):
    bits = np.count_nonzero(A & 1)
    total += (bits * (N - bits)) << shamt
    A >>= 1
    if not A.any():
        break
print(total % MOD)