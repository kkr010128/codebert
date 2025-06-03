from collections import deque
N = int(input())
g = {i: deque() for i in range(1,N+1)} #1-index
for i in range(1, N+1):
    u, k, *v = map(int, input().split())
    for j in v:
        g[u].append(j)
        
seen = [0]*(N+1) #1-index
que = deque([])
dist = [-1]*(N+1) #1-index

seen[1] = 1
que.append(1)
dist[1] = 0

while que: #queが空になるまで
    q_no = que.popleft()
    if not g[q_no]: continue #点q-noから他の点に伸びていない
    
    for next_v in g[q_no]:
        if seen[next_v] == 1: continue #訪問済
        
        seen[next_v] = 1 #訪問済にする
        dist[next_v] = dist[q_no] + 1 #距離情報を格納
        que.append(next_v) #queに追加

for i in range(1, N+1):
    print(i, dist[i])
