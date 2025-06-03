def gcd(a, b):
	if a==0:
		return b
	else:
		return gcd(b%a, a)

X = int(input())
LCM = X*360/gcd(360, X)
print(int(LCM/X))


#a, b = map(int, input().split())
#print(gcd(a, b))

