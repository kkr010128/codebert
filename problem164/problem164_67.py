A, B, C, D = map(int, input().split())

while A >= 0 and C >= 0:
    if C <= B:
        print('Yes')
        break
    else:
        C = C - B

    if A <= D:
        print('No')
        break
    else:
        A = A - D