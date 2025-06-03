H, W, M = map(int, input().split())

HW = set()
sum_h = [0]*H; sum_w = [0]*W
max_sum_h = max_sum_w = 0
for _ in range(M):
    h, w = map(lambda x:int(x)-1, input().split())
    HW.add((h, w))
    sum_h[h] += 1
    sum_w[w] += 1
    max_sum_h = max(max_sum_h, sum_h[h])
    max_sum_w = max(max_sum_w, sum_w[w])

hs = []; ws = []
for i in range(H):
    if sum_h[i] == max_sum_h: hs.append(i)
for i in range(W):
    if sum_w[i] == max_sum_w: ws.append(i)

ans = max_sum_h + max_sum_w - 1
for h in hs:
    for w in ws:
        if (h, w) in HW: continue
        print(ans + 1)
        exit()
print(ans)
