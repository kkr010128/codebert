
while True:
    x,y = input().split()
    x = int(x)
    y = int(y)
    if x==0 and y==0:
        break
    elif x<y:
        print(x,y)
    elif x>=y:
        print(y,x)

    
