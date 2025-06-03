H, W, M = map(int, input().split())
targets = [list(map(int, input().split())) for _ in range(M)]
x_counter = [0 for _ in range(W + 1)]
y_counter = [0 for _ in range(H + 1)]
y_index = []
x_index = []
check = 0

for i in range(M):
    x, y = targets[i]
    y_counter[x] += 1
    x_counter[y] += 1

y_max, x_max = max(y_counter), max(x_counter)

for i in range(H + 1):
    if y_counter[i] == y_max:
        y_index.append(i)

for j in range(W + 1):
    if x_counter[j] == x_max:
        x_index.append(j)

y_index = set(y_index)
x_index = set(x_index)

check = len(y_index) * len(x_index)
for k in range(M):
    r, c = targets[k]
    if r in y_index and c in x_index:
        check -= 1

print(y_max + x_max if check > 0 else y_max + x_max -1)
