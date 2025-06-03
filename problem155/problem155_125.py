from collections import defaultdict
N, M = map(int, input().split())
H = list(map(int, input().split()))

edges = defaultdict(list)

for _ in range(M):
    a, b = map(lambda x:int(x)-1, input().split())
    edges[a].append(b)
    edges[b].append(a)

ans = 0
for i in range(N):
    ok = True
    for adj in edges[i]:
        if H[adj] >= H[i]:
            ok = False
            break
    if ok:
        ans += 1
print(ans)
