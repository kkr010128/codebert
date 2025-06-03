import numpy as np

n = int(input())
arr = np.array([[int(x) for x in input().split()] for _ in range(n)])
med_a = np.median(arr[:, 0])
med_b = np.median(arr[:, 1])

if n % 2 == 0:
    print(int(med_b * 2 - med_a * 2 + 1))
else:
    print(int(med_b - med_a + 1))
