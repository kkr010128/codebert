from collections import deque
N,M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int, input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)

used = [-1]*N
for i in range(N):
    if used[i] >= 0:
        continue
    q = deque()
    q.append(i)
    used[i] = i
    while q:
        temp = q.popleft()
        for e in E[temp]:
            if used[e] == i:
                continue
            used[e] = i
            q.append(e)

L = [0]*N
for c in used:
    L[c] += 1
ans = max(L)
print(ans)