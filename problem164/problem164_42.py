A, B, C, D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)
i = 0

for i in range(100):
    C = (C - B)
    if C <= 0:
        print('Yes')
        break
    else:
        A = A - D
        if A <= 0:
            print('No')
            break
