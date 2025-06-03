def gcd(a,b):
	a,b=max(a,b),min(a,b)
	return a if b==0 else gcd(b,a%b)
x=int(input())
g=gcd(360,x)
print(360//g)