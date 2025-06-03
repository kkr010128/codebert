import collections

N = int(input())
UKV = [list(map(int,input().split())) for _ in range(N)]

dist = [-1]*N
que = collections.deque()

G = [[]]*N
for ukv in UKV:
    G[ukv[0]-1] = sorted(ukv[2:])

dist[0] = 0
que.append(1)

while len(que) != 0:
    v = que.popleft()
    for nv in G[v-1]:
        if dist[nv-1] != -1:
            continue
        dist[nv-1] = dist[v-1] + 1
        que.append(nv)

for i,d in enumerate(dist):
    print(i+1, d)
