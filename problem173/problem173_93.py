import numpy as np

N = int(input())

ans = 0
for i in range(1, N + 1):
    if ((i % 3) != 0) & ((i % 5) != 0):
        ans += i

print(ans)