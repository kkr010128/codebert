def cgd(x,y):
	while(True):
		r=x%y
		if r==0:
			m=y
			break
		x=y
		y=r
	
	return m

a,b=map(int,input().split())
if a>b:
	m=cgd(a,b)
elif a<b:
	m=cgd(b,a)
else:
	m=a
print(m)
	
