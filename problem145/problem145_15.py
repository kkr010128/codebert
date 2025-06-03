from collections import deque

N, M = map(int, input().split())

G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

ls = deque([0])
ans = [-1] * N
ans[0] = 0
while len(ls) > 0:
    v = ls.popleft()

    for next_v in G[v]:
        if ans[next_v] != -1:
            continue
        ans[next_v] = v
        ls.append(next_v)

if -1 in ans:
    print("No")
else:
    print("Yes")
    for i in range(1, N):
        print(ans[i]+1)