h, w, k = map(int, input().split())
mat = [input() for i in range(h)]
num = 0
ans = [[0]*w for _ in range(h)]
heights = [0]*h
for i in range(h):
    for j in range(w):
        if mat[i][j] == "#":
            heights[i] += 1
hs = []
for v in range(h):
    if heights[v] >= 1:
      hs.append(v)
for i in range(len(hs)):
    h1 = 0
    h2 = h-1
    if i >= 1:
        h1 = hs[i-1] + 1
    if i < len(hs)-1:
        h2 = hs[i]
    ws = []
    for j in range(h1, h2+1):
        for k in range(w):
            if mat[j][k] == "#":
                ws.append(k)
    ws.sort()
    for j in range(len(ws)):
        w1 = 0
        w2 = w-1
        if j >= 1:
            w1 = ws[j-1]+1
        if j < len(ws)-1:
            w2 = ws[j]
        num += 1
        for k in range(h1, h2+1):
            for l in range(w1, w2+1):
                ans[k][l] = num
for i in range(h):
    print(*ans[i])

