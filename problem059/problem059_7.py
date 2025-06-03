rc = input().split()
r, c = map(int, rc)

ss= [[int(i) for i in input().split()] for j in range(r)]
colsum = [0 for i in range(c+1)]

for row in ss:
    row.append(sum(row))
    colsum = [x+y for (x, y) in zip(colsum, row)]
    print(' '.join(map(str, row)))

print(' '.join(map(str, colsum)))