n,a,b=map(int,input().split())
if (a+b)%2==0:
    print((b-a)//2)
else:
    if n-b>=a-1:
        print((a+b-1)//2)
    else:
        print(n+(1-a-b)//2)
