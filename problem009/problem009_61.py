n = int(input())
G = [[] for _ in range(n)]
for _ in range(n):
    u, k, *v = [int(i) for i in input().split()]
    G[u - 1] = v
NIL = 100
Q = [[1, 0]]
F = []
D = [NIL for _ in range(n)]
while Q != []:
    u, d = Q.pop(0)
    if d < D[u-1]:
        D[u-1] = d
    if u not in F:
        F.append(u)
    for v in G[u-1]:
        if v not in F:
            Q.append([v, d+1])
'''
for ni in range(1, n):
    Q = [[ni+1, 0]]
    F = []
    while Q != []:
        u, d = Q.pop(0)
        if u == 1 and d < D[ni]:
            D[ni] = d
        if u not in F:
            F.append(u)
        for v in G[u-1]:
            if v not in F:
                Q.append([v, d+1])
'''
for ni in range(n):
    if D[ni] == NIL:
        print(ni+1, -1)
    else:
        print(ni+1, D[ni])
