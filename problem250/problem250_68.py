x=int(input())
if x==2:
    print(2)
else:
    while True:
        cnt=0
        if x%2==0:
            x+=1
            continue
        for i in range(2,x):
            if x%i==0:
                cnt=1
                continue
        if cnt==1:
            x+=1
        else:
            print(x)
            break