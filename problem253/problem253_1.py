n,a,b=map(int,input().split())
if a>b: a,b=b,a

if (a-b)%2==0: print((b-a)//2)
else: print(min(a-1,n-b)+1+(b-a-1)//2)
