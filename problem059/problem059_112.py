r, c = map(int, input().split())

rows = []
for i in range(r):
    row = list(map(int, input().split()))
    row.append(sum(row))
    rows.append(row)

erow = [0 for i in range(c + 1)]
for row1 in rows:
    print(" ".join(str(s) for s in row1))
    for i in range(c + 1):
        erow[i] += row1[i]

print(" ".join(str(s) for s in erow))