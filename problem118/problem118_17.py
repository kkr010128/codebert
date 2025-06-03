import numpy as np

N = int(input())

count = 0
for i in range(1, N+1):
    count += (N // i) * (i + i * (N//i)) // 2


print(count)