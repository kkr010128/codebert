import math

N = int(input())

count = 0
for A in range(1, N):
    for B in range(1, math.ceil(N/A)):
        if A * B < N:
            count += 1
print(count)