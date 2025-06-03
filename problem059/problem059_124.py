r, c = map(int, input().split())
sheet = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    sheet[i].append(sum(sheet[i]))
new_row = []
for j in range(c+1):
    sum_col = 0
    for i in range(r):
        sum_col += sheet[i][j]
    new_row.append(sum_col)
sheet.append(new_row)

for i in range(r+1):
    print(' '.join(str(x) for x in sheet[i]))