import numpy as np
n = int(input())
A = list(map(int, input().strip().split()))
arr = np.array(A)


print(' '.join(map(str, np.argsort(arr) + 1)))
