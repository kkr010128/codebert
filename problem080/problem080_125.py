import numpy as np
N = int(input())
max_z = -np.Inf
min_z = np.inf
max_w = -np.Inf
min_w = np.inf
for _ in range(N):
    x, y = map(int, input().split())
    z = x + y
    w = x - y
    max_z = max(max_z, z)
    min_z = min(min_z, z)
    max_w = max(max_w, w)
    min_w = min(min_w, w)
print(max(max_z-min_z, max_w-min_w))