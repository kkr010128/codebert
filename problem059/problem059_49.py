r, c = map(int, input().split())

row_lists = []
column = []

for i in range(r):
    rows = list(map(int, input().split()))
    row_sum = sum(rows)
    rows.append(row_sum)
    row_lists.append(rows)

for j in range(c+1):
    tmp_list = []
    for i in range(r):
        tmp = row_lists[i][j]
        tmp_list.append(tmp)
    sum_tmp_list = sum(tmp_list)
    column.append(sum_tmp_list)

# output
for i in range(r):
    print(' '.join(map(str, row_lists[i])))

print(" ".join(map(str, column)))
