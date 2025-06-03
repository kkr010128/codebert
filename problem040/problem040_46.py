n=map(int,raw_input().split())
if n[0]<=n[1]<=n[2]:
	a=n[0]
	b=n[1]
	c=n[2]
elif n[0]<=n[2]<=n[1]:
	a=n[0]
	b=n[2]
	c=n[1]
elif n[1]<=n[0]<=n[2]:
	a=n[1]
	b=n[0]
	c=n[2]
elif n[1]<=n[2]<=n[0]:
	a=n[1]
	b=n[2]
	c=n[0]
elif n[2]<=n[0]<=n[1]:
	a=n[2]
	b=n[0]
	c=n[1]
else:
	a=n[2]
	b=n[1]
	c=n[0]
print a,b,c