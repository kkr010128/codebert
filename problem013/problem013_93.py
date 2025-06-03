N = input()
d = -999999999
R = input()
for i in range(N-1):
	r = input()
	d = max(d,(r-R))
	R = min(R,r)
print d