INF = float('inf')

H, W = map(int, input().split())
Sss = ['#'*(W+2)] + ['#'+input()+'#' for _ in range(H)] + ['#'*(W+2)]

def convGrid2Graph(Sss):
    dxys = [(-1,0), (1,0), (0,-1), (0,1)]
    sizeX, sizeY = len(Sss)-2, len(Sss[0])-2

    numV = sizeX * sizeY
    adjL = [[] for _ in range(numV)]
    for x in range(1, sizeX+1):
        for y in range(1, sizeY+1):
            if Sss[x][y] != '.': continue
            z = (x-1)*sizeY + (y-1)
            for dx, dy in dxys:
                x2, y2 = x+dx, y+dy
                if Sss[x2][y2] != '.': continue
                z2 = (x2-1)*sizeY + (y2-1)
                adjL[z].append(z2)
    return adjL

def WarshallFloyd(adjList, INF):
    numV = len(adjList)
    D = [[INF]*numV for _ in range(numV)]
    for u, adj in enumerate(adjList):
        for v in adj:
            D[u][v] = 1
        D[u][u] = 0
    for k in range(numV):
        Dk = D[k]
        for i in range(numV):
            Di = D[i]
            Dik = Di[k]
            for j in range(numV):
                D2 = Dik + Dk[j]
                if D2 < Di[j]:
                    D[i][j] = D2
    return D

adjL = convGrid2Graph(Sss)

distss = WarshallFloyd(adjL, INF)

ans = 0
for i in range(H*W):
    for j in range(H*W):
        if distss[i][j] != INF:
            ans = max(ans, distss[i][j])

print(ans)
