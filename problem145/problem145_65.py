from collections import deque
N,M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int, input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)

q = deque()
q.append(0)
ans = [0]*N
while q:
    par = q.popleft()
    for e in E[par]:
        if ans[e] > 0:
            continue
        ans[e] = par+1
        q.append(e)

print("Yes")
for i in range(1, N):
    print(ans[i])