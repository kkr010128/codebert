a,b,n= map(int, input().split())

if a<n:
    if (n-a)>b:
        print(0,0)
    else:
        print(0,b-(n-a))
else:
    print(a-n,b)