while input()!='0':
    n=list(map(int,input().split()))
    b=len(n)
    a=sum(n)/b
    print((sum((x-a)**2 for x in n)/b)**0.5)