while(True):
    a=list(map(int,input().split()))
    if(a[0]==0 and a[1]==0):
        break
    for x in range(a[0]):
        if x==0 or x==a[0]-1:
            print("#"*a[1])
        else:
            print("#"+"."*(a[1]-2)+"#")
    print()