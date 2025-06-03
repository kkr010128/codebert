n,a,b=map(int,input().split())
s=a+b
if n%s==0:
    print(int(n/s)*a)
else:
    if n%s>=a:
        print(int(n//s+1)*a)
    else:
        print(int(n//s)*a+n%s)