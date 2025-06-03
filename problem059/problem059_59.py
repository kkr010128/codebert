# coding: utf-8

row, col = map(int, input().split())
spreadsheet = []

for i in range(row):
    val = list(map(int, input().split()))
    val.append(sum(val))
    spreadsheet.append(val)

for r in spreadsheet:
    print(' '.join(map(str, r)))

last_row = []
for j in range(len(spreadsheet[0])):
    col_sum = 0
    for i in range(len(spreadsheet)):
        col_sum += spreadsheet[i][j]
    last_row.append(col_sum)

print(' '.join(map(str, last_row)))

