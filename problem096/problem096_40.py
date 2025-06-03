nd=input().split()
n=int(nd[0])
d=int(nd[1])
count=0
z=d*d
for i in range(0,n):
	xy=input().split()
	x=int(xy[0])
	y=int(xy[1])
	if(x*x+y*y<=z):
		count+=1
print(count)
