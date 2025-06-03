h, w, m = map(int, input().split())
table = []
sum_rows = [0 for i in range(h)]
sum_cols = [0 for i in range(w)]
for i in range(m):
    h_, w_ = map(int, input().split())
    table.append((h_, w_))
    sum_rows[h_-1] += 1
    sum_cols[w_-1] += 1

r = max(sum_rows)
c = max(sum_cols)
ans_ = (r + c)
count = 0
for i in range(m):
    if ans_ == (sum_rows[table[i][0]-1]+sum_cols[table[i][1]-1]):
        count += 1

if count == (sum_rows.count(r) * sum_cols.count(c)):
    print(ans_-1)
else:
    print(ans_)