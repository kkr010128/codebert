h,w,K = map(int, input().split())
g = [[0]*w for _ in range(h)]
for i in range(h):
    s=input()
    for j in range(w):
        g[i][j] = s[j]
ans=1001001001
for i in range(1<<(h-1)):
    seg = [0]*h
    segnow = 0
    for j in range(h-1):
        if i & 1 << j:
            segnow += 1
        seg[j+1] = segnow

    segnow += 1
    flag = True
    div = 0
    cnt = [0 for _ in range(segnow)]
    for j in range(w):
        now = [0]*segnow
        for k in range(h):
            if g[k][j] == '1':
                cnt[seg[k]] += 1
                now[seg[k]] += 1
                if cnt[seg[k]] > K:
                    div+=1
                    for l in range(segnow):
                        cnt[l] = now[l]
        if max(now)>K:
            continue
    ans = min(ans,segnow-1+div)
print(ans)