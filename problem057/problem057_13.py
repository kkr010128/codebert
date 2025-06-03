while True:
    z=list(map(int,input().split()))
    if z == [-1,-1,-1]:
        break
    if z[0]==-1 or z[1]==-1:
        print('F')
    elif z[0]+z[1]>=80:
        print('A')
    elif z[0]+z[1] >=65:
        print('B')
    elif z[0]+z[1] >=50 or z[2] >=50:
        print('C')
    elif z[0]+z[1] >=30 :
        print('D')
    else :
        print("F")