H, W, K = map(int, input().split())
cake = [input() for _ in range(H)]
rows = []
has_strawberry = False
for i in range(H):
    if "#" in cake[i]:
        if has_strawberry:
            rows.append(i)
        else:
            has_strawberry = True

rows += [H]

cols = [[] for _ in range(len(rows))]
prev_r = 0
for r in range(len(rows)):
    has_strawberry = False
    for j in range(W):
        if any(cake[i][j] == "#" for i in range(prev_r, rows[r])):
            if has_strawberry:
                cols[r].append(j)
            else:
                has_strawberry = True
    cols[r].append(W)
    prev_r = rows[r]

ans = [[-1] * W for _ in range(H)]
curr_color = 1
prev_r = 0
for r in range(len(rows)):
    prev_c = 0
    for c in range(len(cols[r])):
        for i in range(prev_r, rows[r]):
            for j in range(prev_c, cols[r][c]):
                ans[i][j] = curr_color
        curr_color += 1
        prev_c = cols[r][c]
    prev_r = rows[r]
[print(*row) for row in ans]
