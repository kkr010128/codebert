n,a,b = map(int,input().split())

if (b-a)%2==0:
    print((b-a)//2) 
else:
    m = min(b-1,n-a)
    M = min(a-1,n-b)+(b-a-1)//2+1
    print(min(m,M))