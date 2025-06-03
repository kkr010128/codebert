x=int(input())
if x<100:
    print(0)
else:
    n=x//100
    y=x%100
    if y==0:
        print(1)
    else:
        if int((y+4)//5)<=n:
            print(1)
        else:
            print(0)