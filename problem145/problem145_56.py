N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)
start = 0
queue = [start]
pre = [None]*N
pre[0] = 0
while queue:
    v = queue.pop(0)
    for i in adj[v]:
        if pre[i] is None:
            pre[i] = v
            queue.append(i)
if None in pre:
    print("No")
else:
    print("Yes")
    for p in pre[1:]:
        print(p+1)