import numpy as np
N, M = map(int, input().split())
A = np.array(list(map(int, input().split())))
A.sort()
A = A[::-1] / A.sum()
# print(f'{A=}')

ans = 'Yes' if A[M - 1] >= 1 / 4 / M else 'No'
print(ans)
