import numpy as np

A=[list(map(int, input().split())) for _ in range(3)]
N=int(input())
B=[int(input()) for _ in range(N)]

for b in B:
	for i in range(3):
		for j in range(3):
			if A[i][j]==b:A[i][j]=0
			
ans_axis0=np.sum(np.array(A),axis=0)
ans_axis1=np.sum(np.array(A),axis=1)
ans_naname=[A[0][0]+A[1][1]+A[2][2],A[0][2]+A[1][1]+A[2][0]]

#print(A,ans_axis0,ans_axis1,ans_naname)

if 0 in ans_axis0 or 0 in ans_axis1 or 0 in ans_naname:
	print("Yes")
else:
	print("No")