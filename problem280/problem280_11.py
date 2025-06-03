def dist(x, y, i, j):
    dx = x[i] - x[j]
    dy = y[i] - y[j]
    return (dx * dx + dy * dy) ** 0.5

n = int(input())
x = [0] * n
y = [0] * n

for i in range(n):
    x[i], y[i] = map(int, input().split())

ans = 0
for i in range(n):
    for j in range(i + 1, n):
       ans += dist(x, y, i, j) * 2 / n

print(ans)
