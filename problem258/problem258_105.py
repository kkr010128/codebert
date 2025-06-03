n=int(input())
if n%2==0:
	r=0
	i=1
	while 2*5**i<=n:
		r+=n//(2*5**i)
		i+=1
	print(r)
else:
	print(0)
