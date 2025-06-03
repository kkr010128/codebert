import numpy as np

N = int(input())
X = np.array(list(map(int, input().split())))

X = np.sort(X)
minX = X[0]
maxX = X[-1]
ans = 999999999

for i in range(minX, maxX+1, 1):
    x = (X - i) ** 2
    total = np.sum(x)
    ans = min(ans, total)

print(ans)