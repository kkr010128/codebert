import sys
input = sys.stdin.readline
H, W, M = map(int, input().split())
bombs = []
rows = [[]for _ in range(H)]
cols = [[]for _ in range(W)]
for _ in range(M):
    h, w = map(lambda x: int(x)-1, input().split())
    bombs.append((h, w))
    rows[h].append(w)
    cols[w].append(h)

max_row = 0
row_idx = set()
for i, row in enumerate(rows):
    if max_row < len(row):
        max_row = len(row)
        row_idx = {i}
        continue
    elif max_row == len(row):
        row_idx.add(i)

max_col = 0
col_idx = set()
for i, col in enumerate(cols):
    if max_col < len(col):
        max_col = len(col)
        col_idx = {i}
        continue
    elif max_col == len(col):
        col_idx.add(i)

ans = max_row+max_col
points = len(row_idx)*len(col_idx)
if M < points:
    print(ans)
else:
    for i, j in bombs:
        if i in row_idx and j in col_idx:
            points -= 1
    if points == 0:
        print(ans-1)
    else:
        print(ans)
