r, c = map(int, input().split(' '))

matrix = []
total_cols = [0 for i in range(c+1)]

for i in range(r):
    rows  = list(map(int, input().split(' ')));

    total = sum(rows)
    rows.append(total)

    total_cols = [ total_cols[i] + x for i, x in enumerate(rows) ]

    matrix.append(rows)

matrix.append(total_cols)

for row in matrix:
    print(' '.join([str(i) for i in row]))