import numpy as np
[N, D] = map(int, input().split())
X, Y = np.zeros(N), np.zeros(N)

for i in range(N):
    [x, y] = map(int, input().split())
    X[i], Y[i] = x, y

dist = np.sqrt(X * X + Y * Y)
print(len(np.where(dist <= D)[0]))
