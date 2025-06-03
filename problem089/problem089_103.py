H,W,M = map(int,input().split())

hlist = [0]*H
wlist = [0]*W
sets = set()
for i in range (M):
    h,w = map(lambda x: int(x)-1,input().split())
    hlist[h]+=1
    wlist[w]+=1
    sets.add((h,w))

hmax = 0
hind = []
for i in range(H):
    if hmax < hlist[i]:
        hmax = hlist[i]
        hind = [i]
    elif hmax == hlist[i]:
        hind.append(i)


wmax = 0
wind = []
for i in range(W):
    if wmax < wlist[i]:
        wmax = wlist[i]
        wind = [i]
    elif wmax == wlist[i]:
        wind.append(i)


flag = False
for h in hind:
    for w in wind:
        if (h,w) not in sets:
            flag = True
            break
    if flag:
        break

if flag:
    print(hmax + wmax)
else:
    print(hmax + wmax - 1)
