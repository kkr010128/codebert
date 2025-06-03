H,W,K = map(int,input().split())
C = [[int(i) for i in input()] for _ in range(H)]
ans = float("inf")

for i in range(1<<(H-1)):
    start = [0]
    end = []
    for j in range(H-1):
        if i & (1 << j):
            j += 1
            start.append(j)
            end.append(j)
    end.append(H)
    L = len(end)
    cnt = [0]*L
    dcnt = L-1
    fail = False
    for w in range(W):
        div = False
        idx = 0
        tmp = [0]*L
        for s,e in zip(start,end):
            for h in range(s,e): tmp[idx] += C[h][w]
            if tmp[idx] > K: 
                fail = True
                break
            if cnt[idx] + tmp[idx] > K:
                div = True
                cnt = tmp[:]
            else:
                cnt[idx] += tmp[idx]
            idx += 1
        if fail: break
        if div: dcnt += 1
    if fail: continue
    ans = min(dcnt,ans)

print(ans)