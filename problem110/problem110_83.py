H,W,K = map(int,input().split())
c = []
row = [0]*H
col = [0]*W
total = 0

for i in range(H):
    c.append(list(input()))
    for j in range(W):
        if c[i][j] == '#':
            row[i] += 1
            col[j] += 1
            total += 1

#print(total)
ans = 0
for i in range(2**(H+W)):
    x = [0]*(H+W)
    ii = i
    for j in range(H+W):
        x[j] = ii % 2
        ii//=2
    #print(x)
    D = 0
    for j in range(H):
        D += row[j]*x[j]
    for j in range(H,H+W):
        D += col[j-H]*x[j]

    for j in range(H):
        for k in range(W):
            if c[j][k] == '#':
                D -= x[j]*x[H+k]
    
    if total -D == K:
        ans += 1
    #print(x,ans)

print(ans)