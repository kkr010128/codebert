def solve():
    T1, T2 = map(int, input().split())
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())

    if A1 < B1 and A2 < B2:
        return 0
    elif A1 > B1 and A2 > B2:
        return 0

    C1, C2 = B1-A1, B2-A2

    if C1*T1 + C2*T2 == 0:
        return 'infinity'

    if C1*T1 + C2*T2 < 0:
        C1, C2 = -C1, -C2

    if abs(C1*T1) > abs(C2*T2):
        return 0

    x1, x2 = T1, 2*T1+T2
    y1, y2 = C1*T1, 2*C1*T1+C2*T2

    x = -y1 * (x2-x1) // (y2-y1) + x1

    z = x-T1
    T = T1+T2
    num = z//T
    ans = num*2
    dist = C1*T1 + (C1*T1 + C2*T2)*num
    if dist != 0:
        ans += 1

    return int(ans)


print(solve())
