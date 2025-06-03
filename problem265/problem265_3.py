import numpy as np

N = int(input())
X_low = N // 1.08
X_high = int(X_low + 1)

if np.floor(X_low * 1.08) == N:
    print(X_low)
elif np.floor(X_high * 1.08) == N:
    print(X_high)
else:
    print(':(')


