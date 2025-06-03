h1, m1, h2, m2, k = map(int, input().split())

dh = h2 - h1
dm = m2 - m1

if dm < 0:
    dh -= 1
    dm += 60

wm = dh*60 + dm
ans = wm - k

print(ans)