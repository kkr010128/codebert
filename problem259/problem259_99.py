from collections import deque

n, u, v = map(int, input().split())
u -= 1 
v -= 1
tree = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(lambda x : int(x) - 1, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque()
q.append((u, 0))
depth = [0] * n

visited = set()
while q:
    p, d = q.popleft()
    depth[p] = d
    visited.add(p)
    for x in tree[p]:
        if not x in visited:
            q.append((x, d+1))


q.append((v, 0))
visited.clear()
max_case = max(depth[v] - 1, 0)
while q:
    p, d = q.popleft()
    visited.add(p)
    is_leaf = True
    for x in tree[p]:
        if not x in visited:
            q.append((x, d+1))
            is_leaf = False
    if is_leaf and depth[p] < d:
        max_case = max(max_case, d - 1)
print(max_case)
