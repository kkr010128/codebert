import collections
h, w, m = map(int, input().split())
h = [None]*m
w = [None]*m
for i in range(m):
    u, v = map(int, input().split())
    h[i] = u
    w[i] = v
hc = collections.Counter(h)
wc = collections.Counter(w)
hm = hc.most_common()[0][1]
hs = set([])
for hi, ci in hc.most_common():
    if ci == hm:
        hs.add(hi)
    else:
        break
wm = wc.most_common()[0][1]
ws = set([])
for wi, ci in wc.most_common():
    if ci == wm:
        ws.add(wi)
    else:
        break
cnt = 0
for i in range(m):
    if h[i] in hs and w[i] in ws:
        cnt += 1
if cnt == len(hs)*len(ws):
    print(hm + wm -1)
else:
    print(hm + wm)