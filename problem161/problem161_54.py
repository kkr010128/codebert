import math

a,b,c=list(map(int, input().split()))
if b<=c:
	print(math.floor(a*(b-1)/b))
else:
	print(math.floor(a*c/b)-a*(math.floor(c/b)))