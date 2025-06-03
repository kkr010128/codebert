n, m, l = map(int, input().split())

alst = []
for i in range(n):
    a = list(map(int, input().split()))
    alst.append(a)
    
blst = []
for i in range(m):
    b = list(map(int, input().split()))
    blst.append(b)
    
for i in range(n):
    clst = []
    for j in range(l):
        c = 0
        for k in range(m):
            c += alst[i][k]*blst[k][j]
        clst.append(c)
    print(*clst) 
