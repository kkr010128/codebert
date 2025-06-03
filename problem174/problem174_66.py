import numpy as np
k = int(input())
x = np.arange(1,k+1)
# np.ufunc.outer: c_ij = f(a_i, b_j)
a = np.gcd.outer(np.gcd.outer(x,x),x)
print(a.sum())