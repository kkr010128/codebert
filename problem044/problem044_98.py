x,y,z= map(int,input().split())
n= 0
c= x
for i in range(y-c+1):
	if(z%x==0):
		n+= 1
	x+= 1
print(n)