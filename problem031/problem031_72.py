while(True):
    n=int(input())
    if(n==0):
        break
    val=list(map(int, input().split()))
    sum=0
    for i in val:
        sum+=i
    mean=sum/n
    disp=0
    for i in val:
        disp+=(i-mean)**2
    disp=disp/n
    print(disp**0.5)
    


