from collections import deque
n = int(input())
G = [None for i in range(n)]

for i in range(n):
    u,k,*vs = map(int,input().split())
    G[u-1] = [e-1 for e in vs]


dist = [-1]*n #全頂点を未訪問に初期化(-1)で未訪問
que = deque([0])   #初期条件 (頂点 0 を初期ノードとする) 
dist[0] = 0 #0を訪問済み

while len(que)>0:
    now = que.popleft()
    for i in G[now]:
        if dist[i] != -1:
            continue
        dist[i] = dist[now] + 1 #新たな頂点wについて距離情報を更新してキューに追加する
        que.append(i)

for i in range(n):
    print(i+1,dist[i])
