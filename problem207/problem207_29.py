import numpy as np
A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = []
for j in range(N):
    b = int(input())
    B.append(b)
A = np.array(A)
B = np.array(B)
boolean_matrix = np.isin(A, B)
if boolean_matrix.sum(axis=1).max() >= 3 or \
   boolean_matrix.sum(axis=0).max() >= 3 or \
   np.diag(boolean_matrix).sum() >= 3 or \
   np.diag(np.fliplr(boolean_matrix)).sum() >= 3:
    print('Yes')
else:
    print('No')