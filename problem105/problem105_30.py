import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))
A_odd = A[::2]
print(np.sum(A_odd % 2))