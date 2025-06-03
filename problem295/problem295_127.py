import sys
printn = lambda x: sys.stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
DBG = True # and False
BIG = 9999999999

def ddprint(x):
  if DBG:
    print(x)

def ws(dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],
                              dist[i][k]+dist[k][j])

n,m,l = inm()
dst = [ [] for i in range(n) ]
for i in range(m):
    a,b,c = inm()
    dst[a-1].append((b-1,c))
    dst[b-1].append((a-1,c))

dist1 = [ [BIG]*n for i in range(n) ]
for i in range(n):
    dist1[i][i] = 0
    for j,c in dst[i]:
        dist1[i][j] = c

ws(dist1)

dist2 = [ [BIG]*n for i in range(n) ]
for i in range(n):
    dist2[i][i] = 0
    for j in range(n):
        if dist1[i][j] <= l:
            dist2[i][j] = 1

ws(dist2)

q = inn()
for i in range(q):
    s,t = inm()
    d = dist2[s-1][t-1]
    print(d-1 if d<BIG else -1)
