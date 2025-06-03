import numpy as np

h, w, k = map(int, input().split())

grid = []
for _ in range(h):
    grid.append(list(map(str, input().rstrip())))
grid = (np.array(grid)).reshape(h, -1)

x, y = np.where(grid == "#")

arr = np.zeros((h, w), dtype=int)
arr[x, y] = np.arange(1, k+1)

np.maximum.accumulate(arr, axis=1, out=arr)

for w in range(w - 2, -1, -1):
    arr[:, w] += arr[:, w+1] * (arr[:, w] == 0)

for i in range(1, h):
    if arr[i, -1] == 0:
        arr[i] += arr[i - 1]

for j in range(h - 1, -1, -1):
    if arr[j, -1] == 0:
        arr[j] += arr[j+1]

for i in range(h):
    print(*arr[i])