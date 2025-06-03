h, w, k = map(int, input().split())
s = [input() for _ in range(h)]

t = [[0] * w for _ in range(h)]
n = 0
rows = []
for i in range(h):
    if s[i].count("#") == 0:
        rows.append(i)
    else:
        if s[i][0] == "#":
            for j in range(w):
                if s[i][j] == "#":
                    n += 1
                t[i][j] = n
        else:
            n += 1
            f = 0
            for j in range(w):
                if f and s[i][j] == "#":
                    n += 1
                elif s[i][j] == "#":
                    f = 1
                t[i][j] = n

if rows != [] and rows[-1] == h-1:
    for k in range(h)[::-1]:
        if t[k][j] != 0:
            for j in range(w):
                t[rows[-1]][j] = t[k][j]
            break
        
for i in rows:
    for k in range(i+1, h):
        if t[k][j] != 0:
            for j in range(w):
                t[i][j] = t[k][j]
            break

for i in range(h):
    print(*t[i])