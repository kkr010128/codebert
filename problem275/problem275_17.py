a=[300000,200000,100000]
x,y=map(int,input().split())
ans=0
if x<4:
	ans+=a[x-1]
if y<4:
	ans+=a[y-1]
if x==y==1:
	ans+=400000
print(ans)