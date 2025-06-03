h, w = map(int,input().split())
s = [input() for i in range(h)]

def f(i, j):
    t = [[-1]*w for j in range(h)]
    t[i][j] = 0
    q = [(i,j)]
    while q:
        y, x = q.pop(0)
        if y - 1 >= 0 and s[y-1][x] != "#" and t[y-1][x] == -1:
            t[y-1][x] = t[y][x] + 1
            q.append((y-1,x))
        if y + 1 < h and s[y+1][x] != "#" and t[y+1][x] == -1:
            t[y+1][x] = t[y][x]+1
            q.append((y+1,x))
        if x - 1 >= 0 and s[y][x-1] != "#" and t[y][x-1] == -1:
            t[y][x-1] = t[y][x] + 1
            q.append((y,x-1))
        if x + 1 < w and s[y][x+1] != "#" and t[y][x+1] == -1:
            t[y][x+1] = t[y][x] + 1
            q.append((y,x+1))
    return max(max(tt) for tt in t)
result = 0
for i in range(h):
    for j in range(w):
        if s[i][j] != "#":
            result = max(result,f(i,j))
print(result)



    
        
    
    
