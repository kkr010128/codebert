a,b,c=list(map(int,raw_input().split()))
if 4*a*b < (c-(a+b))*(c-(a+b)) and c > (a+b):
	print("Yes")
	exit(0)
print("No")