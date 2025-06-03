import sys
T1, T2, A1, A2, B1, B2 = map(int, sys.stdin.read().split())
a1, b1 = T1*A1, T1*B1
a2, b2 = T2*A2, T2*B2
sa, sb = a1+a2, b1+b2
if sa==sb:
    print("infinity")
    exit()
if sa < sb:
    a1, a2, b1, b2, sa, sb = b1, b2, a1, a2, sb, sa
# 2*n-1 回以上出会うか
ok = 0
ng = 10**1800
a = 0
while ok+1 < ng:
    c = (ok+ng)//2
    if (c-1)*sa+a1 <= (c-1)*sb+b1:
        if (c - 1) * sa + a1 == (c - 1) * sb + b1:
            a = -1
        ok = c
    else:
        ng = c
if ok > 10**1799:
    print("a")
    print("infinity")
else:
    print(max(ok*2-1+a, 0))
