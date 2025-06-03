n,a,b=map(int,input().split())

if a+b ==0:
    print(0)
else:
    c = n//(a+b)
    d = n%(a+b)

    if d <= a:
        print(a*c+d)
    else:
        print(a*c+a)