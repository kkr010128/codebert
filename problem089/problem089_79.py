from collections import defaultdict
h, w, m = map(int, input().split())
targets = defaultdict(int)
targets_count_yoko = defaultdict(int)
targets_count_tate = defaultdict(int)
for _ in range(m):
    y, x = map(int, input().split())
    y -= 1
    x -= 1
    targets_count_yoko[x] += 1
    targets_count_tate[y] += 1
    targets[(y, x)] = -1

max_row = max(targets_count_yoko.values())
max_line = max(targets_count_tate.values())
y_idx = defaultdict(bool)
x_idx = defaultdict(bool)
max_count_x = 0
max_count_y = 0
for i in range(w):
    if targets_count_yoko[i] == max_row:
        x_idx[i] = True
        max_count_x += 1
for i in range(h):
    if targets_count_tate[i] == max_line:
        y_idx[i] = True
        max_count_y += 1


ans = max_line + max_row
kumi = max_count_x*max_count_y
for key_y, key_x in targets.keys():
    if y_idx[key_y] and x_idx[key_x]:
        kumi -= 1
    if kumi == 0:
        break

if kumi == 0:
    print(ans-1)
else:
    print(ans)

