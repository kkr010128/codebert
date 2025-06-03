from collections import deque
N, M = map(int, input().split())
nodes = [set() for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    nodes[a-1].add(b-1)
    nodes[b-1].add(a-1)
ans = [-1 for i in range(N)]
ans[0] = 0
q = deque([])
q.append(0)

cur = 0
done = set()
done.add(0)
while q:
    node = q.popleft()
    for x in nodes[node]:
        if x in done:
            continue
        q.append(x)
        done.add(x)
        ans[x] = node + 1
if -1 in ans:
    print('No')
else:
    print('Yes')
    for x in ans[1:]:
        print(x)