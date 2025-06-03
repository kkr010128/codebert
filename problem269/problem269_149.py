import math

T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

if A1 > B1:
    F1, F2 = A1, A2
    S1, S2 = B1, B2
else:
    F1, F2 = B1, B2
    S1, S2 = A1, A2

oi = F1 * T1 - S1 * T1
nuki = S2 * T2 - F2 * T2 - oi

if nuki == 0:
    print("infinity")
elif nuki > 0:
    enc = oi // nuki * 2
    if oi % nuki != 0:
        enc = enc + 1
    print(enc)
else:
    print(0)