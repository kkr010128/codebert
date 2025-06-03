# Belongs to : midandfeed aka asilentvoice
n, m, l = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for i in range(n)]
b = [[int(x) for x in input().split()] for i in range(m)]
ans = []

for i in range(n):
	rtemp = []
	for j in range(l):
		temp = 0
		for k in range(m):
			temp += (a[i][k] * b[k][j])
		rtemp.append(temp)
	ans.append(rtemp)
	
for row in ans:
	print(" ".join(map(str, row)))