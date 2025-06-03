h, w, k = map(int,input().split())
s = [input() for _ in range(h)]
a = [[0]*w for _ in range(h)]

# 番号を数える
strno = 1
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            a[i][j] = strno
            strno += 1

# 番号を埋める           
for i in range(h):
    for j in range(w-1):
        if a[i][j+1] == 0:
            a[i][j+1] = a[i][j]
for i in range(h):
    for j in range(w-1):
        if a[i][w-j-2] == 0:
            a[i][w-j-2] = a[i][w-j-1]
            
for i in range(h-1):
    for j in range(w):
        if a[i+1][j] == 0:
            a[i+1][j] = a[i][j]
for i in range(h-1):
    for j in range(w):
        if a[h-i-2][j] == 0:
            a[h-i-2][j] = a[h-i-1][j]
            
for row in a:
    print(*row)
