import sys
a=[map(int,i.split())for i in sys.stdin]
for i,j in a:
	c,d=i,j
	while d:
		if c > d:c,d = d,c
		d%=c
	print(c,i//c*j)