n,a,b=map(int,input().split())
if a%2==b%2:
    print((b-a)//2)
    exit()
if a-1<n-b:
    print(a+(b-a-1)//2)
else:
    print(n-b+1+(b-a-1)//2)