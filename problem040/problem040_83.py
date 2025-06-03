a,b,c=map(int,input().split())
if a>b:
	a,b = b,a
if c<a:
	a,b,c = c,a,b
if c<b:
	a,b,c = a,c,b
print(a,b,c)