from collections import deque
import copy
H, W = map(int, input().split())
S = [input() for _ in range(H)]

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(H*W):
        for i in range(H*W):
            for j in range(H*W):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d


d = [[float("inf")]*(H*W) for i in range(H*W)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(H-1):
    for j in range(W-1):
        if S[i][j] == ".":
            if S[i+1][j] == ".":
                d[i*W+j][(i+1)*W+j] = 1
                d[(i+1)*W+j][i*W+j] = 1
            if S[i][j+1] == ".":
                d[i*W+j][i*W+(j+1)] = 1
                d[i*W+(j+1)][i*W+j] = 1
for i in range(W-1):
    if S[H-1][i] == "." and S[H-1][i+1] == ".":
        d[(H-1)*W+i][(H-1)*W+(i+1)] = 1
        d[(H-1)*W+(i+1)][(H-1)*W+i] = 1
for i in range(H-1):
    if S[i][W-1] == "." and S[i+1][W-1] == ".":
        d[i*W+(W-1)][(i+1)*W+(W-1)] = 1
        d[(i+1)*W+(W-1)][i*W+(W-1)] = 1

for i in range(H*W):
    d[i][i] = 0 #自身のところに行くコストは０

ans = 0
data = warshall_floyd(d)
for items in data:
    for item in items:
        if item != float("inf"):
            ans = max(ans, item)
print(ans)
