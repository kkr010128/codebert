col,row = map(int,input().split())
matrix = []
vector = []
for _ in range(col):
	matrix.append([int(j) for j in input().split()])

for _ in range(row):
	vector.append(int(input()))

for i in range(col):
	ans = 0
	for x,y in zip(matrix[i],vector):
		ans += x * y
	print(ans)