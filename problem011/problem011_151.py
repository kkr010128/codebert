def getResult(a,b):
	if a<b:
		a,b=b,a
	while b!=0:
		r = a%b
		a = b
		b = r
	return a
a,b = map(int,input().strip().split())
print(getResult(a,b))