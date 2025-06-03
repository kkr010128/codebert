r, c = [int(s) for s in input().split()]
rows = [[0 for i in range(c + 1)] for j in range(r + 1)]

for rc in range(r):
    in_row = [int(s) for s in input().split()]
    for cc, val in enumerate(in_row):
        rows[rc][cc] = val
        rows[rc][-1] += val
        rows[-1][cc] += val
        rows[-1][-1] += val
    
for row in rows:
    print(' '.join([str(i) for i in row]))