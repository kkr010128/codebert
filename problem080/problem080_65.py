N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    X.append(x)
    Y.append(y)
    
points = []
for x, y in zip(X, Y):
    points.append((
        x + y,
        x - y
    ))
print(max(max(dim) - min(dim) for dim in zip(*points)))