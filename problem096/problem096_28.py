N, D = map(int, input().split())
x = []
y = []
for i in range(N):
    coords = list(map(int, input().split()))
    x.append(coords[0])
    y.append(coords[1])

count = 0
for i in range(N):
    if (x[i]**2 + y[i]**2) ** 0.5 <= D:
        count += 1

print(count)