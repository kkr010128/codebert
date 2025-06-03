import numpy as np

count = 0
n,d = map(int,input().split())

for _ in range(n):
    p,q = map(int, input().split())
    if np.sqrt(p**2+q**2) <= d:
        count += 1
print(count)