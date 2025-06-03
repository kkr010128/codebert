T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
Ad = A1 * T1 + A2 * T2
Bd = B1 * T1 + B2 * T2
if Ad == Bd:
    print('infinity')
else:
    if Bd > Ad:
        Ad, Bd = Bd, Ad
        A1, B1 = B1, A1
    if A1 > B1:
        print(0)
    else:
        num = (B1 - A1) * T1 // (Ad - Bd)
        if (B1 - A1) * T1 % (Ad - Bd) == 0:
            print(num * 2)
        else:
            print(num * 2 + 1)
