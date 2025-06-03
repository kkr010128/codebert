T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
d1 = (A1 - B1) * T1
d2 = d1 + (A2 - B2) * T2
if (d1 > 0 and d2 > 0) or (d1 < 0 and d2 < 0):
    print(0)
    exit()
if d2 == 0:
    print('infinity')
    exit()
d1 = abs(d1)
d2 = abs(d2)
if d1 % d2 == 0:
    print(d1 // d2 * 2)
else:
    print(1 + d1 // d2 * 2)
