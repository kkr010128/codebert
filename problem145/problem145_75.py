from collections import deque

n, m = [int(w) for w in input().split()]
links = [[] for i in range(n + 1)]
mark = [-1] * (n + 1)

for i in range(m):
    a, b = [int(w) for w in input().split()]
    links[a].append(b)
    links[b].append(a)

q = deque([1])
while q:
    now = q.popleft()
    for l in links[now]:
        if mark[l] == -1:
            q.append(l)
            mark[l] = now

if -1 in mark[2:]:
    print("No")
else:
    print("Yes")
    print("\n".join([str(w) for w in mark[2:]]))
