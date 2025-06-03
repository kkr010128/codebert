while True:
    case=input().split()
    x=int(case[0])
    y=int(case[1])
    
    if x==0 and y==0:
        break
    else:
        if x<y:
            print(x,y)
        else:
            print(y,x)