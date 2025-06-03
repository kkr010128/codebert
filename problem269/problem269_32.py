t=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if a[0]>b[0]:
    a,b=b,a
p=t[0]*(a[0]-b[0])
q=t[1]*(a[1]-b[1])
if p+q==0:
    print('infinity')
elif p+q<0:
    print(0)
else:
    k=-p//(p+q)
    if -p%(p+q)==0:
        print(2*k)
    else:
        print(2*k+1)
