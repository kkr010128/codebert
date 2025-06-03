import numpy as np


N = int(input())

X = int(np.ceil(N/1.08))
if np.floor(X*1.08)!=N:
    X = ':('

print(X)