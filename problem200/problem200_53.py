a,b,m = map(int,input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
x = []
y = []
c = []
for i in range(m):
	xs,ys,cs = map(int,input().split())
	x.append(xs)
	y.append(ys)
	c.append(cs)

ans1 = 10**10
for j in range(m):
	if ans1 >= a[x[j]-1] + b[y[j]-1] - c[j]:
		ans1 = a[x[j]-1] + b[y[j]-1] - c[j]
ans2 = min(a)+min(b)
print(min(ans1,ans2))