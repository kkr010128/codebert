import sys
import numpy as np

input = sys.stdin.buffer.readline
N = int(input())
A = np.array(list(map(int, input().split())))

MOD = 10**9 + 7

answer = 0
for n in range(63):
    B = (A >> n) & 1
    x = np.count_nonzero(B)
    y = N - x
    x *= y
    for _ in range(n):
        x = x * 2 % MOD
    answer += x
answer %= MOD
print(answer)
