t=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if a[0]*t[0]+a[1]*t[1]==b[0]*t[0]+b[1]*t[1]:
    print('infinity')
elif a[0]*t[0]+a[1]*t[1]>b[0]*t[0]+b[1]*t[1]:
    if a[0]*t[0]>b[0]*t[0]:
        print(0)
    elif a[0]*t[0]==b[0]*t[0]:
        print(1)
    else:
        n=t[0]*(b[0]-a[0])
        m=t[0]*(a[0]-b[0])+t[1]*(a[1]-b[1])
        q=n//m
        if n%m==0:
            print(2*q)
        else:
            print(2*q+1)
else:
    if a[0]*t[0]<b[0]*t[0]:
        print(0)
    elif a[0]*t[0]==b[0]*t[0]:
        print(1)
    else:
        n=-t[0]*(b[0]-a[0])
        m=-t[0]*(a[0]-b[0])-t[1]*(a[1]-b[1])
        q=n//m
        if n%m==0:
            print(2*q)
        else:
            print(2*q+1)