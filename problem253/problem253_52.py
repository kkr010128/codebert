n,a,b = map(int,input().split())
if (b - a)%2 == 0:
    x = (b - a)//2
    y = min(max(a-1,b-1),max(n-a,n-b))
    print(min(x,y))
else:
    p = max(a-1,b-1)
    q = max(n-a,n-b)
    r = a-1+1+(b-(a-1)-1-1)//2
    s = n-b+1+(n-(n-b+1)-a)//2
    #print(p,q,r,s)
    print(min(p,q,r,s))