from itertools import product
import numpy as np

n, _, x = map(int, input().split())
arr1 = np.array([list(map(int, input().split())) for _ in range(n)])
ans = 1200000
if np.all(arr1.sum(0)[1:] >= x):
    for i in product((0, 1), repeat=n):
        arr2 = (i * arr1.T).sum(1)
        if np.all(arr2[1:] >= x):
            ans = min(ans, arr2[0])
    print(ans)
else:
    print(-1)