h, w, k = map(int, input().split())
s = [input() for _ in range(h)]
a = [[0]*w for _ in range(h)]
cnt = 0
later = []
for i in range(h):
    if '#' not in s[i]: continue
    later.append(i)
    fst = False
    idx = -1
    for j in range(w):
        if not fst and not s[i][j] == '#':
            continue
        if not fst and s[i][j] == '#':
            idx = j
        if s[i][j] == '#':
            fst = True
            cnt += 1
        a[i][j] = cnt
    for j in range(idx):
        a[i][j] = a[i][idx]

for i in later:
    if i >= h-1: break
    for j in range(w):
        k = i
        while k < h-1:
            if a[k+1][j] == 0:
                a[k+1][j] = a[k][j]
                k += 1
            else:
                break
                
if later[0] != 0:
    for i in range(later[0], 0, -1):
        for j in range(w):
            a[i-1][j] = a[i][j]
for ans in a:
    print(*ans)