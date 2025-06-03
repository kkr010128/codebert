n,m,l = map(int,input().split())
A,B,C = [],[],[]
for i in range(n):
	A.append(list(map(int,input().split())))
for ii in range(m):
	B.append(list(map(int,input().split())))
for k in range(n):
	ans = []
	for s in range(l):
		cul = 0
		for kk in range(m):
			cul += A[k][kk] * B[kk][s]
		ans.append(cul)
	ans = list(map(str,ans))
	print(" ".join(ans))
