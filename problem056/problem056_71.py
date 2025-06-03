# (c) midandfeed
n, m = [int(x) for x in input().split()]
a = []
b = []
for _ in range(n):
	z = [int(x) for x in input().split()]
	a.append(z)
	
for _ in range(m):
	b.append(int(input()))
	
for i in range(n):
	ans = 0
	for j in range(m):
		ans += a[i][j]*b[j]
	print(ans)