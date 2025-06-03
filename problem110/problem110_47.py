h,w,k = map(int,input().split())
ls = [str(input()) for _ in range(h)]
a = [[] for _ in range(2**h)]
b = [[] for _ in range(2**w)]
for i in range(2**h):
    for j in range(h):
        if (i>>j)&1:
            a[i].append(j)
for s in range(2**w):
    for l in range(w):
        if (s>>l)&1:
            b[s].append(l)
p = 0
for e in range(2**h):
    for f in range(2**w):
        cnt = 0
        for g in range(len(ls)):
            if g not in a[e]:
                di = list(ls[g])
                for t in range(len(di)):
                    if t not in b[f]:
                        if di[t] == "#":
                            cnt += 1
        if cnt == k:
            p += 1
print(p)