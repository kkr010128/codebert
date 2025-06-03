import numpy as np
count = 0
n, d = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())
    if np.sqrt(x**2 + y**2) <= d:
        count +=1
print(count)