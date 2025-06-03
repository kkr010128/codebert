import math
a,b,c=map(int,input().split())
eps = 0.00000000000001
if 4*a*b<(c-a-b)**2 and (c-a-b)>0:
	print('Yes')
else:
	print('No')