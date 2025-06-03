n = int(input())
sp, sm = [], []
res = 0
for _ in range(n):
    s = input()
    m = len(s)

    l, tl = 0, 0
    for i in range(m):
        if s[i] == ')':
            tl -= 1
        else:
            tl += 1
        l = min(l, tl)

    r, tr = 0, 0
    for i in range(m):
        if s[m-1-i] == '(':
            tr -= 1
        else:
            tr += 1
        r = min(r, tr)

    res += tl
    if tl >= 0:
        sp.append((l, tl))
    else:
        sm.append((r, tr))

if res != 0:
    print('No')
    exit()

sp.sort(key=lambda x: -x[0])
sm.sort(key=lambda x: -x[0])


xp = len(sp)
cur = 0
for l, tl in sp:
    if cur + l < 0:
        print('No')
        exit()
    cur += tl

cur = 0
for r, tr in sm:
    if cur + r < 0:
        print('No')
        exit()
    cur += tr

print('Yes')

