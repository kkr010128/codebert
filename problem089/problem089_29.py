h, w, m = list(map(int, input().split()))
count_row = [0 for _ in range(h)]
count_col = [0 for _ in range(w)]
max_col = 0
max_row = 0
max_row_index = []
max_col_index = []
M = set()
for i in range(m):
    mh, mw = list(map(int, input().split()))
    M.add((mh-1, mw-1))
    count_row[mh-1] += 1
    count_col[mw-1] += 1
    if count_row[mh-1] > max_row:
        max_row = count_row[mh-1]
        max_row_index = [mh-1]
    elif count_row[mh-1] == max_row:
        max_row_index.append(mh-1)
    
    if count_col[mw-1] > max_col:
        max_col = count_col[mw-1]
        max_col_index = [mw-1]
    elif count_col[mw-1] == max_col:
        max_col_index.append(mw-1)
# max_row_index = [i for i, v in enumerate(count_row) if v == max(count_row)]
# max_col_index = [i for i, v in enumerate(count_col) if v == max(count_col)]
# ans = max(count_row) + max(count_col) -1
ans = max_col + max_row -1

if len(max_col_index)*len(max_row_index) > m:
    ans += 1
else:
    flag = False
    for i in max_row_index:
        for j in max_col_index:
            if (i, j) not in M:
                ans += 1
                flag = True
                break
        if flag:
            break
print(ans)