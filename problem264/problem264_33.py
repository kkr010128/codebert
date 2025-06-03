M1,D1=list(map(int, input().split()))
M2,D2=list(map(int, input().split()))
if (M1==M2-1 or M1-M2==11) and D2==1:
    print(1)
else:
    print(0)