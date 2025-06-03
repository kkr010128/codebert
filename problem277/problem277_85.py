h,w,k = map(int,input().split())
lst = []
cut1 = []
for i in range(h):
    l = input()
    if '#' in l:
        cut1.append(i)
    lst.append(l)
res = [[float('inf')]*w for _ in range(h)]

cut2 = []
for c in cut1:
    tmp_cut = []
    for j in range(len(lst[c])):
        if lst[c][j]=='#':
            tmp_cut.append(j)
    cut2.append(tmp_cut)

cnt = 1
for e,i in enumerate(cut1):
    for j in cut2[e]:
        res[i][j] = cnt
        cnt += 1

for r in res:
    mn = min(r)
    mx = max(r)
    if (mn==mx) and (mn==float('inf')):
        pass
    else:
        mx = max(set(r) - {float('inf')})
        if mn==mx:
            for i in range(w):
                if r[i] == float('inf'):
                    r[i] = mn
        else:
            for i in range(w):
                if r[i] == float('inf'):
                    r[i] = mn
                else:
                    mn = min(mx, r[i])

for i in range(w):
    tmp = []
    for j in range(h):
        if res[j][i] != float('inf'):
            tmp.append(res[j][i])
    num = min(tmp)
    for j in range(h):
        if res[j][i] == float('inf'):
            res[j][i] = num
        else:
            num = res[j][i]

for r in res:
    print(*r)