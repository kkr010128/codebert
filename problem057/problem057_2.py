while True:
    m,f,r=map(int, input().split())
    s=m+f
    if m==-1 and f==-1 and r==-1:
        break
    elif m==-1 or f==-1 or s <30:
        print('F')
    elif s <50 and r <50:
        print('D')
    elif s <65:
        print('C')
    elif s <80:
        print('B')
    else:
        print('A')