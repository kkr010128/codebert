from collections import Counter
n, m = map(int, input().split())
group = [None for _ in range(n)]
connected = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    connected[a].append(b)
    connected[b].append(a)
# print(connected)
for i in range(n):
    if group[i] is not None: continue
    newly_visited = [i]
    group[i] = i
    while len(newly_visited) > 0:
        new = newly_visited.pop()
        for j in connected[new]:
            if group[j] is not None: continue
            group[j] = i
            newly_visited.append(j)
# print(Counter(group))
print(len(Counter(group)) - 1)
