def Warshall_Floyd(dist,n,restoration=False):
    next_point = [[j for j in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[j][k] > dist[j][i] + dist[i][k]:
                    next_point[j][k] = next_point[j][i]
                    dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
    if restoration:
        return dist,next_point
    else:
        return dist

n,m,l = map(int,input().split())
inf = 10**18
dist = [[inf for i in range(n)] for j in range(n)]

for i in range(n):
    dist[i][i] = 0

for i in range(m):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    if c <= l:
        dist[a][b] = c
        dist[b][a] = c

dist = Warshall_Floyd(dist,n)
route = [[inf for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            route[i][j] = 0
        elif dist[i][j] <= l:
            route[i][j] = 1

route = Warshall_Floyd(route,n)

q = int(input())


for i in range(q):
    s,t = map(int,input().split())
    s -= 1
    t -= 1
    print(route[s][t]-1 if route[s][t] < inf else -1)