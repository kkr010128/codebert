A, B, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

x = []
y = []
c = []
for i in range(m):
	xx, yy, cc = map(int, input().split())
	x.append(xx)
	y.append(yy)
	c.append(cc)


ans = min(a) + min(b)

for i in range(m):
	ans = min(ans,a[x[i]-1] + b[y[i]-1] - c[i])
print (ans)