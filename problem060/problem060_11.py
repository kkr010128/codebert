n,m,l=map(int,raw_input().split())
matA=[map(int,raw_input().split()) for i in range(n)]
matB=[map(int,raw_input().split()) for j in range(m)]
for i in range(n):
	for j in range(l):
		 print sum([matA[i][k]*matB[k][j] for k in range(m)]),
	print	