n,a,b=map(int,input().split())
i=n%(a+b)
if i>a:
    print(a*(n//(a+b))+a)
else:
    print(a*(n//(a+b))+i)