X,Y=map(int,input().split())
MOD=10**9+7

def modinv(a):
	return pow(a,MOD-2,MOD)

x=(2*Y-X)//3
y=(2*X-Y)//3

if (2*Y-X)%3!=0 or (2*X-Y)%3!=0 or x<0 or y<0:
	print(0)
else:
	r=1
	n=x+y
	k=min(x,y)
	for i in range(k):
		r*=(n-i)
		r*=modinv(i+1)
		r%=MOD
	print(r)
