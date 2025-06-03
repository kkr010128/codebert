#全点対間最短経路を求めるアルゴリズム

def warshall_floyd(d):
    #d[i][j]:iからjに行く最短経路
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**9)

n, m , l = map(int, input().split())

INF = 10 ** 11
d = [[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
        x, y, z = map(int, input().split())
        if z <= l:
            d[x][y] = z
            d[y][x] = z #無向グラフならつける

for i in range(1,n+1):
    d[i][i] = 0

    

ss = warshall_floyd(d)



for i in range(1,n+1):
    for j in range(1,n+1):
        if ss[i][j] <= l:
            ss[i][j] = 1


#補給回数
vv = warshall_floyd(ss)

for i in range(1,n+1):
    for j in range(1,n+1):
        if vv[i][j] == INF:
            vv[i][j] = -1

q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    if vv[x][y] != -1:
    	print(vv[x][y]-1)
    else:
      	print(vv[x][y])