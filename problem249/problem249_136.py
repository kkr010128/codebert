a,b,k=map(int,input().split())
c=max(0,a-k)
d=min(b,b-(k-a))
if d<0:
    print(c,"0")
else:
    print(c,d)