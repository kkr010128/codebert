T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
diff1 = (A1 - B1) * T1
diff2 = (A2 - B2) * T2

if diff1 > 0:
    diff1, diff2 = -1 * diff1, -1 * diff2

if diff1 + diff2 < 0:
    print(0)
elif diff1 + diff2 == 0:
    print('infinity')
else:
    q, r = divmod(-diff1, diff1 + diff2)
    print(2*q + (1 if r != 0 else 0))