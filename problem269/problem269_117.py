T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
d1 = T1 * (A1 - B1)
d2 = T2 * (A2 - B2)
if d1 > 0 and d1 + d2 > 0:
    print(0)
elif d1 < 0 and d1 + d2 < 0:
    print(0)
elif d1 + d2 == 0:
    print("infinity")
else:
    if d1 < 0:
        d1 = -d1
        d2 = -d2
    ok = 0
    ng = (d1 + d1) // (-d1 - d2) + 1
    x = 0
    while ok + 1 < ng:
        mid = (ok + ng) // 2
        s = mid * (d1 + d2)
        if s + d1 > 0:
            ok = mid
        elif s + d1 == 0:
            ok = mid
            ng = ok + 1
            x = -1
        else:
            ng = mid
    print(ng * 2 - 1 + x)