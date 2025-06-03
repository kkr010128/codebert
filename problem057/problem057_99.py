
while True:
    m,f,r = map(int, raw_input().split())
    s = m + f
    if m == -1 and f == -1 and r == -1: break
    elif m == -1 or f == -1 or s < 30: g=5
    elif 30 <= s and s < 50:
        if r >= 50: g=2
        else: g=3
    elif 50 <= s and s < 65: g=2
    elif 65 <= s and s < 80: g=1
    else: g=0
    print 'ABCDEF'[g]
