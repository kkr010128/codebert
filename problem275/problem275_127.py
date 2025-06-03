X,Y=map(int,input().split())
if X==1 :
    x=300000
elif X==2 :
    x=200000
elif X==3 :
    x=100000
else :
    x=0
if Y==1 :
    y=300000
elif Y==2 :
    y=200000
elif Y==3 :
    y=100000
else :
    y=0
if X==1 and Y==1 :
    print(x+y+400000)
else :
    print(x+y)