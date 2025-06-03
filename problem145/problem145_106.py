from collections import deque

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
sign = [-1] * N

for _ in range(M):
    A, B = map(int, input().split())
    edge[A - 1].append(B - 1)
    edge[B - 1].append(A - 1)

d = deque([0])

while d:
    cur = d.popleft()
    for adj in edge[cur]:
        if sign[adj] == -1:
            sign[adj] = cur
            d.append(adj)

print("Yes")
for i in range(1, N):
    print(sign[i] + 1)