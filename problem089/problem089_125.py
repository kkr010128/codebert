H, W, M = map(int, input().split())

h_list = [0 for i in range(H)]
w_list = [0 for i in range(W)]

point = {}
for _ in range(M):
    h, w = map(int, input().split())
    h_list[h - 1] += 1
    w_list[w - 1] += 1
    point[(h - 1, w - 1)] = 1

hmax = 0
wmax = 0
hmap = {}
wmap = {}
for i, h in enumerate(h_list):
    if hmax <= h:
        hmax = h
        hmap.setdefault(h, []).append(i)
for i, w in enumerate(w_list):
    if wmax <= w:
        wmax = w
        wmap.setdefault(w, []).append(i)
# print(hmap)
# print(wmap)
# hmax = max(h_list)
# wmax = max(w_list)
h_index = h_list.index(hmax)
w_index = w_list.index(wmax)

for h in hmap[hmax]:
    for w in wmap[wmax]:
        if (h, w) not in point:
            print(hmax + wmax)
            exit(0)

print(hmax + wmax - 1)