import itertools
import numpy as np

h, w, k = map(int, input().split())
c = [input() for _ in range(h)]

count = 0
for ph in itertools.product([0, 1], repeat=h):
    for pw in itertools.product([0, 1], repeat=w):
        squares = np.array([[1 if cell == '#' else -1 for cell in row] for row in c])
        squares[np.array(ph) == 1, :] *= 0
        squares[:, np.array(pw) == 1] *= 0
        count += np.count_nonzero(squares == 1) == k

print(count)
