x,y,r=map(int,raw_input().split())
c=0
for i in range(x,y+1):
	if r%i==0:
		c=c+1
print c		