n=int(input())
if n==0:
	p=0
	print("%.9f"%p)
elif n&1:
	p=(n//2)+1
	print("%.9f"%(p/n))
else:
	p=n//2
	print("%.9f"%(p/n))	