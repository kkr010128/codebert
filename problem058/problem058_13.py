while True:
	k=map(int,raw_input().split(" "))
	if k[0]==k[1]==0:
		break
	ct=0
	a=0
	b=0
	c=0	
	max=k[0]
	sum=k[1]
	a=max+1
	while True:
		a-=1
		b=a-1
		c=sum-a-b
		if not a>c:
			print ct
			break
		while b>c:
			if c>0:
				ct+=1
			b-=1
			c+=1