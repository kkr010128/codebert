n = int(input())

count = [[0] * 10 for _ in range(10)]

for i in range(1, n + 1):
    now = str(i)
    pre, pos = int(now[0]), int(now[-1])
    if pos == 0: continue
    count[pre][pos] += 1

res = 0
for i in range(1, 10):
    for j in range(1, 10):
        res += count[i][j] * count[j][i]

print(res)

