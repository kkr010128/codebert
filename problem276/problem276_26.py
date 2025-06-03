import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())))

A_cs = A.cumsum()
A_cs = A_cs - A_cs[-1]/2
div = np.abs(A_cs).argmin()

print(abs(A[:div+1].sum() - A[div+1:].sum()))