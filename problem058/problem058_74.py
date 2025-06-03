
while(True):
    i=0
    a=list(map(int,input().split()))
    if(a[0]==0 and a[1]==0):
        break
    for x in range(2,a[0]):
        sum=a[1]-x
        for y in range(1,x):
            if (sum-y<a[0]+1 and sum-y>x):
                i+=1
    print(i)    