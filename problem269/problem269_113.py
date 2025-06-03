T1, T2 = map(int,input().split())
A1, A2 = map(int,input().split())
B1, B2 = map(int,input().split())
if T1*A1 + T2*A2 == T1*B1 + T2*B2:
    print("infinity")
else:
    if T1*A1 + T2*A2 > T1*B1 + T2*B2:
        A1, B1 = B1, A1
        A2, B2 = B2, A2
    if T1*A1 < T1*B1:
        print("0")
    else:
        forward = T1*A1 - T1*B1
        shrink = (T1*B1 + T2*B2) - (T1*A1 + T2*A2)
        #print(str(forward))
        #print(str(shrink))
        if forward % shrink == 0:
            print(str(2*forward//shrink))
        else:
            print(str((forward//shrink + 1)*2 - 1))