N = int(input())

tree = [[] for _ in range(N)]

for _ in range(N):
    u, k, *v = map(int, input().split())
    tree[u-1] = v

ans = [float('inf') for _ in range(N)]
ans[0] = 0

from collections import deque

q = deque([(0, 0)])

while q:
    p, d = q.popleft()
    for c in tree[p]:
        if ans[c-1] > d+1:
            ans[c-1] = d+1
            q.append((c-1, d+1))

for i in range(N):
    if ans[i] == float('inf'):
        print(i+1, -1)
    else:
        print(i+1, ans[i])
