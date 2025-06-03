import copy

h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]
ans = 0

for i in range(1 << (h + w)):
    l = copy.deepcopy(c)
    for p in range(h):
        if i >> p & 1:
            l[p] = ['r'] * w
    for m in range(w):
        if i >> (m + h) & 1:
            for o in range(h):
                l[o][m] = 'r'
    s = ''
    for i in range(h):
        s += ''.join(l[i])
    if s.count('#') == k:
        ans += 1
print(ans)