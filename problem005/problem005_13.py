import sys
for n in sys.stdin:
	l=map(int,n.split())
	b=l[0]*l[1]
	u=[max(l),min(l)]
	while u[1]!=0:
		u=[u[1],u[0]%u[1]]
	print "%d %d"%(u[0],b/u[0])