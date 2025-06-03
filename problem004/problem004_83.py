n=int(input())
for i in range(n):
	x=list(map(int,input().split()))
	a,b,c=sorted(x)
	if a**2+b**2==c**2:
		print('YES')
	else:
		print('NO')