a,b,n=map(int,input().split())
if b<=n:
    x=b-1
else:
    x=n
print(int((a*x/b//1)-(a*(x/b//1))))