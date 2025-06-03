T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

C1 = A1 - B1
C2 = A2 - B2

if C1 * C2 >= 0:
    print(0)

else:
    if C1 < 0:
        C1, C2 = -C1, -C2
    P = T1 * C1
    Q = P + T2 * C2
    if Q > 0:
        print(0)
    elif Q == 0:
        print('infinity')
    else:
        hi = 10**18
        lo = -1
        while hi - lo > 1:
            mid = (hi + lo) // 2
            if Q * mid + P <= 0:
                hi = mid
            else:
                lo = mid
        if Q * hi + P == 0:
            print(hi * 2)
        else:
            print(hi * 2 - 1)