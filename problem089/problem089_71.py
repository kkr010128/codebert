from collections import Counter
ans = 0
H, W, M = map(int, input().split())
HW = set()
Hlist, Wlist = [], []
for _ in range(M):
    h, w = map(int, input().split())
    Hlist.append(h)
    Wlist.append(w)
    HW.add((h,w))

cntH = Counter(Hlist)
cntW = Counter(Wlist)

maxhk, maxhv = cntH.most_common()[0]
ans = max(ans, maxhv)
for i in range(1,1+W):
    tmp = cntW[i]
    if (maxhk, i) in HW:
        tmp -= 1
    ans = max(ans, tmp+maxhv)

maxwk, maxwv = cntW.most_common()[0]
ans = max(ans, maxwv)
for i in range(1,1+H):
    tmp = cntH[i]
    if (i, maxwk) in HW:
        tmp -= 1
    ans = max(ans, tmp+maxwv)

print(ans)
