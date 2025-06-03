M1, D1 = map(int, input().split())
M2, D2 = map(int, input().split())

if M1 in [1, 3, 5, 7, 8, 10, 12]:
    if D1 == 31:
        print(1)
    else:
        print(0)
elif M1 in [4, 6, 9, 11]:
    if D1 == 30:
        print(1)
    else:
        print(0)
elif M1 == 2:
    if D1 == 28:
        print(1)
    else:
        print(0)