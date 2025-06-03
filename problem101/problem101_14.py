def magic(a,b,c,k):
	for i in range(k):
		if(a>=b):
			b*=2
		elif(b>=c):
			c*=2
	if(a < b and b < c):
		print("Yes")
	else:
		print("No")
d,e,f = map(int,input().split())
j = int(input())
magic(d,e,f,j)

