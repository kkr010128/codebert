a,b,n=map(int,input().split())
if a>b and n>b:x=n
else:x=min(n,b-1)
print((a*x)//b-a*(x//b))