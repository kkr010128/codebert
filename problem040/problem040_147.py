a,b,c=map(int, input().split(" "))
	
if a>c :
	k=c
	c=a
	a=k
if c<b :
	k=b
	b=c
	c=k
if b<a :
	k=b
	b=a
	a=k
a,b,c=map(str,(a,b,c))
print(a+' '+b+' '+c)