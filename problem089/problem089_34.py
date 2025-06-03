from collections import defaultdict
h, w, m = map(int, input().split())
targets = []
targets_count_w = defaultdict(int)
targets_count_h = defaultdict(int)
for _ in range(m):
    y, x = map(int, input().split())
    y -= 1
    x -= 1
    targets_count_w[x] += 1
    targets_count_h[y] += 1
    targets.append((y, x))

max_w = max(targets_count_w.values())
max_h = max(targets_count_h.values())
y_idx = defaultdict(bool)
x_idx = defaultdict(bool)
max_count_x = 0
max_count_y = 0
for i in range(w):
    if targets_count_w[i] == max_w:
        x_idx[i] = True
        max_count_x += 1
for i in range(h):
    if targets_count_h[i] == max_h:
        y_idx[i] = True
        max_count_y += 1


ans = max_w + max_h
kumi = max_count_x*max_count_y
for ty, tx in targets:
    if y_idx[ty] and x_idx[tx]:
        kumi -= 1
    if kumi == 0:
        break

if kumi == 0:
    print(ans-1)
else:
    print(ans)

