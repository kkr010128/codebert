r, c = map(int, input().split())

data = []

for y in range(r):
    row = list(map(int, input().split()))
    data.append(row)

colsum = [0 for i in range(c + 1)]
for y in range(r):
    data[y].append(sum(data[y]))
    for x in range(c + 1):
        colsum[x] += data[y][x]

data.append(colsum)

for y in range(r + 1):
    print(*data[y])