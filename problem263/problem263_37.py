import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

MOD = 10 ** 9 + 7

N = int(readline())
A = np.array(read().split(),np.int64)

answer = 0
for n in range(63):
    B = (A >> n) & 1
    x = np.count_nonzero(B)
    y = N - x
    x *= y
    for _ in range(n):
        x *= 2
        x %= MOD
    answer += x
answer %= MOD
print(answer)
