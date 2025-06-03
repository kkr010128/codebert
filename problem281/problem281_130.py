import math
x, y = map(int, input().split())
MOD = 10**9+7
 
def combination(n, r, mod):
	r = min(r, n-r)
	num = 1
	d = 1
	for i in range(1, r+1):
		num = num * (n+1-i) % mod
		d = d * i % mod
	return num * pow(d, mod-2, mod) % mod
if (x+y)%3 != 0:
	print (0)
	exit()
n = (x+y)/3
yy = (2*x-y)/3
xx = (2*y-x)/3
if yy < 0:
  print (0)
  exit()
if xx < 0:
  print (0)
  exit()
if xx.is_integer() and yy.is_integer():
	print (combination(int(xx+yy),int(xx),MOD))
else:
	print (0)