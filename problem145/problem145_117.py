from collections import deque

n, m = map(int, input().split())

way = {}
for i in range(m):
    a, b = map(int, input().split())
    if a not in way:
        way[a] = []
    if b not in way:
        way[b] = []
    way[a].append(b)
    way[b].append(a)

queue = deque([1])
ok = set([1])
ans = [0] * (n+1)

while queue:
    now = queue.popleft()
    for i in way[now]:
        if i in ok:
            continue
        ans[i] = now
        queue.append(i)
        ok.add(i)

print("Yes")
for i in range(2, n+1):
    print(ans[i])
