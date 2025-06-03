import numpy as np

T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

S1 = (A1 - B1) * T1
S2 = (A2 - B2) * T2

if (S1 + S2) == 0:
    print('infinity')
elif np.sign(S1) == np.sign(S2):
    print(0)
elif abs(S1) > abs(S2):
    print(0)
else:
    z = 1 + ((abs(S1)) // abs(S1 + S2)) * 2
    if (abs(S1)) % abs(S1 + S2) == 0:
        z = z -1
    print(z)
