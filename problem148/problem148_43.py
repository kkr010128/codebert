A, B, C, K = input().split()
IA = int(A)
IB = int(B)
IC = int(C)
IK = int(K)
ALL = IA + IB + IC
cn = 0

if IA <= IK:
    cn = cn + IA
    D = IK - IA
    if IB <= D:
        E = D - IB
        cn = cn - E
        print(cn)
    else:
        print(cn)
else:
    print(IK)
