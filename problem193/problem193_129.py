h, w, k = map(int, input().split())
s = [list(map(int, input())) for _ in range(h)]
ans = float("inf")

for sep in range(1 << (h-1)):
    g_id = [0] * h
    cur = 0
    for i in range(h-1):
        g_id[i] = cur
        if sep >> i & 1: cur += 1
    g_id[h-1] = cur
    g_num = cur+1

    ng = False
    for i in range(w):
        tmp = [0] * g_num
        for j in range(h): tmp[g_id[j]] += s[j][i]
        if any([x > k for x in tmp]): ng = True; break
    if ng: continue

    res = g_num-1
    
    gs = [0] * g_num
    for i in range(h):
        gs[g_id[i]] += s[i][0]
    
    for i in range(1, w):
        tmp = gs[::]
        for j in range(h):
            tmp[g_id[j]] += s[j][i]
        if any([x > k for x in tmp]):
            res += 1
            gs = [0] * g_num
        for j in range(h): gs[g_id[j]] += s[j][i]

    ans = min(ans, res)

print(ans)
