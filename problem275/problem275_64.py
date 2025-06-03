X,Y = map(int,input().split())

if X == Y == 1:
    print(1000000)
else:
    if X <= 3 and Y <= 3:
        print(((4-X)+(4-Y))*10**5)
    elif X >= 4 and Y >= 4:
        print(0)
    else:
        print((4-min(X,Y))*10**5)