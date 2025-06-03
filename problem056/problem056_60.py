N,M = map(int,input().split())

n =  [[] for i in range(N)]

for i in range(N):
    n[i] = list(map(int,input().split()))

m = [ 0 for k in range(M)]

for k in range(M):
    m[k] = int(input())

for x in range(N):
    a = 0
    for y in range(M):
        a += n[x][y] * m[y]
    print(a)
