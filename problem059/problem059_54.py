[r,c] = map(int,raw_input().split()) 
D = [[0 for i in range(c+1)] for j in range(r+1)] 
for y in range(r):
    v = map(int,raw_input().split())
    for x in range(c):
        D[y][x] = v[x]
        D[y][c] = D[y][c] + v[x]
        D[r][x] = D[r][x] + v[x]
        D[r][c] = D[r][c] + v[x] 
        
for y in range(r+1):
    s = ''
    for x in range(c+1):
        if x == 0:
            s = str(D[y][x])
        else: s = s + ' ' + str(D[y][x])
    print s