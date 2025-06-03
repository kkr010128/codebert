inf = 10 ** 10

########ワーシャルフロイド法

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

##############################
n,w,L = map(int,input().split()) #n:頂点数　w:辺の数

d = [[inf for i in range(n)] for i in range(n)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(w):
    x,y,z = map(int,input().split())
    x -= 1
    y -= 1
    d[x][y] = z
    d[y][x] = z
for i in range(n):
    d[i][i] = 0 #自身のところに行くコストは０
d = warshall_floyd(d)

D = [[inf for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            D[i][j] = 0
        elif d[i][j] <= L:
            D[i][j] = 1

D = warshall_floyd(D)

Q = int(input())
for i in range(Q):
    s,t = map(int,input().split())
    s -= 1
    t -= 1
    if D[s][t] == inf:
        print(-1)
    else:
        print(D[s][t]-1)


        
