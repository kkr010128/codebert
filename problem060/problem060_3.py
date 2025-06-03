import sys

array_data = map(int, raw_input().split())
n = array_data[0]
m = array_data[1]
l = array_data[2]

a = []
for i in range(n):
	partial_a = map(int, raw_input().split())
	a.append(partial_a)

b = []
for j in range(m):
	partial_b = map(int, raw_input().split())
	b.append(partial_b)

c = []
for i in range(n):
	c.append([])
	for j in range(l):
		c[i].append([])
		wa = 0
		for k in range(m):
			wa += a[i][k] * b[k][j]
		c[i][j] = wa

for i in range(len(c)):
	for j in range(len(c[i])):
		if j != len(c[i])-1:
			sys.stdout.write("{:} ".format(c[i][j]))
		else:
			print(c[i][j])