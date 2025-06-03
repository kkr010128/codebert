import itertools
import numpy as np

def distance(x2,x1,y2,y1):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

routes = list(itertools.permutations(range(N), N))
ans = []

for route in routes:
    dist = 0
    for i in range(1, N):
        dist += distance(X[route[i]], X[route[i-1]], Y[route[i]], Y[route[i-1]])
    ans.append(dist)

print(np.mean(ans))
