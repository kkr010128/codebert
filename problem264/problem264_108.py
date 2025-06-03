M1,D1 = list(map(int,input().split()))
M2,D2 = list(map(int,input().split()))
if (M1 != M2 and M2>M1) or M2 == 1 and M2<M1:
    print(1)
else:
    print(0)