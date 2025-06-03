a,b,c=[int(x) for x in input().split()]
if a%b==0:
	print((a//b)*c)
else:
	print(((a//b)+1)*c)