M1,D1 = map(int, input().split())
M2,D2 = map(int, input().split())
if M1==12 and M2==1 or M1+1==M2:
    print(1)
else:
    print(0)