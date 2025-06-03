mod = 10**9 + 7
def cmb(n,r,mod):
	a=1
	b=1
	r = min(r,n-r)
	for i in range(r):
		a = a*(n-i)%mod
		b = b*(i+1)%mod
	return a*pow(b,mod-2,mod)%mod

X,Y = map(int,input().split())
if (X+Y)%3 != 0:
  ans = 0
else:
  n = (2*X-Y)//3
  m = (2*Y-X)//3
  if n < 0 or m < 0:
    ans = 0
  else:
    ans = cmb(n+m,m,mod)
print(ans)