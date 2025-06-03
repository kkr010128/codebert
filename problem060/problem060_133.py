# ????????????
n,m,l = list(map(int,input().split()))
matrixA,matrixB = [],[]
for i in range(n):
	matrixA.append(list(map(int,input().split())))
for j in range(m):
	matrixB.append(list(map(int,input().split())))

matrix = []
for i in range(l):
	mtr = []
	for j in range(m):
		mtr.append(matrixB[j][i])
	matrix.append(mtr)

matrixC = []
for i in range(l):
	mtr = []
	for j in range(n):
		num_sum = 0
		# print(matrixA[j],matrix[i])
		for a,b in zip(matrixA[j],matrix[i]):
			num_sum += a*b
		mtr.append(num_sum)
	matrixC.append(mtr)

matrix = []
for i in range(n):
	out = ''
	for j in range(l):
		out += str(matrixC[j][i]) + ' '
	print(out[:-1])