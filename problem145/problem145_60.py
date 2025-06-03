n,m = map(int,input().split())

import heapq

def dijkstra(s):
    d = 1
    hq = [(0, s)]
    heapq.heapify(hq) # リストを優先度付きキューに変換
    cost = [float('inf')] * n # 行ったことのないところはinf
    cost[s] = 0 # 開始地点は0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]: # コストが現在のコストよりも高ければスルー
            continue
        for u in e[v]:
            tmp = 1 + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))
    return cost

e = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    a,b = a-1, b-1
    e[a].append(b)
    e[b].append(a) # 有向グラフでは削除

d = dijkstra(0)
# print(d)
# print(e)
ans = [0]*(n)
for i in range(1,n):
    for j in e[i]:
        # print(i,j)
        if d[j] == d[i] - 1:
            ans[i] = j + 1
            continue

print("Yes")
print(*ans[1:], sep="\n")