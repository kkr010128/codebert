T1, T2, A1, A2, B1, B2 = map(int, open(0).read().split())

P = (A1 - B1) * T1
Q = (A2 - B2) * T2

if P > 0:
    P, Q = -P, -Q

if P + Q < 0:
    print(0)
elif P + Q == 0:
    print("infinity")
else:
    S, T = divmod(-P, P + Q)
    print(S * 2 + (T != 0))
