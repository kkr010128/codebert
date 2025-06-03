from sys import stdin

N, D = map(int, input().split())
points = []
for i in range(N):
    X, Y = map(int, stdin.readline()[:-1].split())
    points.append((X, Y))

count = 0
for i in range(N):
    X, Y = points[i]
    d = (X**2 + Y**2) ** 0.5
    if d <= D:
        count += 1

print(count)
