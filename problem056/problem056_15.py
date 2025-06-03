n,m=map(int,input().split())
matA=[list(map(int,input().split())) for i in range(n)]
matB=[int(input()) for i in range(m)]
for obj in matA:
	print(sum(obj[i] * matB[i] for i in range(m)))