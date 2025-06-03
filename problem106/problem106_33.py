import math

n = int(input())
max = int(math.sqrt(n) + 1)
L = [0] * (n + 1)
for x in range(1, max):
    for y in range(1, max):
        for z in range(1, max):
            tmp = x * x + y * y + z * z + x * y + y * z + z * x
            if tmp > n:
                continue
            L[tmp] += 1

for i in range(1, n + 1):
    print(L[i])
