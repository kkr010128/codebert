import numpy as np

a, b, c, d = map(int, input().split())
x = np.array([a, b])
y = np.array([c, d])
z = np.outer(x, y)
print(z.max())