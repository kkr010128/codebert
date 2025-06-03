H,W,K = map(int,input().split())
HW = [list(input()) for _ in range(H)]

ans = [[0 for _ in range(W)] for _ in range(H)]
cnt = 0
mm = []

for h in range(H):
    if not("#" in HW[h]):
        continue
    mm.append(h)
    cnt += 1
    flg = 1

    for w in range(W):
        if HW[h][w]=="#" and not(flg):
            cnt += 1

        ans[h][w]=cnt

        if flg and HW[h][w]=="#":
            flg = 0
            continue

j = 0
for h in range(H):
    if j<len(mm)-1 and h==mm[j]:
        j += 1
        continue
    else:
        ans[h] = ans[mm[j]]
        
        

for h in range(H):
    print(*ans[h])
