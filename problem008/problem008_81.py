def dfs(index):
    global count
    d[index] = count
    count += 1
    for i in field[index]:
        if d[i]:
            continue
        count = dfs(i)
    f[index] = count
    return count + 1

n = int(input())
field = [[0,0]]
for _ in range(n):
    u, k, *v = map(int, input().split())
    field.append(v)
d = [0 for _ in range(n + 1)]
f = [0 for _ in range(n + 1)]

count = 1
for i in range(1, n + 1):
    if d[i]:
        continue
    count = dfs(i)
for i in range(1, n + 1):
    print(i, d[i], f[i])
