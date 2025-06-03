T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

D1 = T1 * A1 - T1 * B1
D2 = T1 * A1 + T2 * A2 - T1 * B1 - T2 * B2

if D1 * D2 > 0:
    print(0)
elif D2 == 0:
    print("infinity")
else:
    D1 = abs(D2 - D1)
    D2 = abs(D2)
    c = (D1 // D2) * 2 - 1
    if D1 % D2 == 0:
        c -= 1
    print(c)
