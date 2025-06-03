import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

H, W, M = map(int, input().split())

rows = [0] * (H + 1)
cols = [0] * (W + 1)

from collections import defaultdict
ng_cols = defaultdict(set)

for _ in range(M):
    h, w = map(int, input().split())
    rows[h] += 1
    cols[w] += 1
    ng_cols[h].add(w)

max_of_rows = max(rows)
max_of_cols = max(cols)
max_rows_index = set()
max_cols_index = set()
for i in range(H + 1):
    if rows[i] == max_of_rows:
        max_rows_index.add(i)
for i in range(W + 1):
    if cols[i] == max_of_cols:
        max_cols_index.add(i)
flag = 0
for i in max_rows_index:
    for j in max_cols_index:
        if j not in ng_cols[i]:
            flag = 1
            break
print(max_of_rows + max_of_cols - 1 + flag)






