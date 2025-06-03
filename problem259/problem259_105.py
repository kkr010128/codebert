import sys, heapq
from collections import defaultdict
from itertools import product, permutations, combinations

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

N, u, v = map(int, input().split())



def dijkstra_heap(s,edge):
#始点sから各頂点への最短距離
    d = [10**20] * N
    used = [True] * N #True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for a,b in edge[s]:
        heapq.heappush(edgelist,a*(10**6)+b)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        #まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge%(10**6)]:
            continue
        v = minedge%(10**6)
        d[v] = minedge//(10**6)
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,(e[0]+d[v])*(10**6)+e[1])
    return d

AB = [list(map(int, input().split())) for _ in range(N-1)]

adjl = [[] for _ in range(N)]
for ab in AB:
    a, b = ab[0]-1, ab[1]-1
    adjl[a].append([1, b])
    adjl[b].append([1, a])

du = dijkstra_heap(u-1, adjl)
dv = dijkstra_heap(v-1, adjl)
dOK = [j for i, j in zip(du, dv) if i < j]

print(int(max(dOK)-1))
