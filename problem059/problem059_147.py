r, c = map(int, input().split())
mat = [list(map(int, input().split())) for i in range(r)]
for row in mat:
    row.append(sum(row))
    print(*row)
colSum = [sum(col) for col in zip(*mat)]
print(*colSum)