N = int(input())
adj_list = []
for _ in range(N):
    line = list(input().split(" "))
    adj_list.append([int(k) - 1 for k in line[2:]])

d = [-1 for _ in range(N)]
f = [-1 for _ in range(N)]
time = 1

visited = set()

def dfs(p):
    global time
    if p in visited:
        return

    d[p] = time
    time += 1
    visited.add(p)
    for ad in adj_list[p]:
        if ad not in visited:
            dfs(ad)
    f[p] = time
    time += 1

for i in range(N):
    dfs(i)

for i in range(N):
    print(f"{i + 1} {d[i]} {f[i]}")
