(r, c) = [int(i) for i in input().split()]
src = []
for _ in range(r):
    row = [int(i) for i in input().split()]
    row.append(sum(row))
    src.append(row)
last_row = [0 for _ in range(c + 1)]
for rc in range(r):
    for cc in range(c+1):
        last_row[cc] += src[rc][cc]
src.append(last_row)

for rc in range(r+1):
    print(' '.join([str(a) for a in src[rc]]))