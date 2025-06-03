[r,c] = raw_input().split()
r = int(r)
c = int(c)
M = []
V = []
for y in range(0,r):
    s = raw_input().split()
    k = []
    for x in range(0,c):
        v = int(s[x])
        k.append(v)
    M.append(k)
    
for y in range(0,c):
    s = int(raw_input())
    V.append(s)
    

for y in range(0,r):
    ss = 0
    for x in range(0,c):
        ss = ss + M[y][x] * V[x]
    print ss