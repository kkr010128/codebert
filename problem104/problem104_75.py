l,r,n=map(int,input().split())
a=(r//n)-(l//n if l!=n else 0)
if l!=r:print(a)
else: print(1)