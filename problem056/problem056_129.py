n, m = map(int, input().split())

mat = []
for i in range(n):
	mat.append(list(map(int, input().split())))

vec = []
for i in range(m):
	vec.append(int(input()))

for i in range(n):
	e = 0
	for j in range(m):
		e += mat[i][j] * vec[j]
	print(e)