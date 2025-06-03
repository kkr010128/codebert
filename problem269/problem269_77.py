T1, T2 = [int(i) for i in input().split()]
A1, A2 = [int(i) for i in input().split()]
B1, B2 = [int(i) for i in input().split()]

d1 = T1*(A1-B1)
d2 = T2*(B2-A2)

if d1 == d2:
    print('infinity')

if d1 * (d2 - d1) < 0:
    print(0)

if d1 * (d2 - d1) > 0:
    if d1 % (d2 - d1) != 0:
        print(d1 // (d2 - d1) * 2+ 1)
    else:
        print(d1 // (d2 - d1) * 2)