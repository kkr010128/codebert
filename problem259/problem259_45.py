N, U, V = map(int, input().split())
G = [set() for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)

stack = [V]
path = []
vs = set([V])
G2 = [set() for _ in range(N+1)]
depth = [0] * (N+1)
while stack:
    v = stack.pop()
    if v > 0:
        path.append(v)
        if v == U:
            tmp = len(path)//2
#            print(path)
            ss = path[-tmp]
        for u in G[v]:
            if u in vs:
                continue
            depth[u] = depth[v] + 1
            G2[v].add(u)
            vs.add(u)
            stack += [-v, u]
    else:
        path.pop()

stack = [ss]
vs = set([ss])
while stack:
    v = stack.pop()
    for u in G2[v]:
        if u in vs:
            continue
        vs.add(u)
        stack.append(u)
#print(vs, depth)
x = 0
for v in vs:
    x = max(depth[v], x)
print(x-1)
