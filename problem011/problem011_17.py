gcd=list(map(int,input().split()))

if gcd[0]<gcd[1]:
	gcd[0],gcd[1]=gcd[1],gcd[0]
while gcd[1]>0:
	r=gcd[0]%gcd[1]
	gcd[0]=gcd[1]
	gcd[1]=r
print(gcd[0])

