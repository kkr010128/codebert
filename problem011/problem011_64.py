n=input().split()
x=int(n[0])
y=int(n[1])
if 1<=x<1000000000 and 1<=y<=1000000000:
	if x>y:
		while y!=0:
			t=y
			y=x%t
			x=t
		print(x)
	else:
		while x!=0:
			t=x
			x=y%t
			y=t
		print(y)
