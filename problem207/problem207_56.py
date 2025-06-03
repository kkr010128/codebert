H = [[0] * 3 for i in range(3)]
A = [[0] * 3 for i in range(3)]

A[0][0],A[0][1],A[0][2] = map(int,input().split())
A[1][0],A[1][1],A[1][2] = map(int,input().split())
A[2][0],A[2][1],A[2][2] = map(int,input().split())

N = int(input())
for i in range(N):
	ball = int(input())
	for l in range(3):
		for c in range(3):
			if A[l][c] == ball:
				H[l][c] = 1
#print(H)
flag = 0
for l in range(3):
	if H[l][0] ==1 and H[l][1] ==1  and H[l][2] ==1:
		flag =1

for c in range(3):
	if H[0][c] ==1 and H[1][c] ==1  and H[2][c] ==1:
		flag =1

if H[0][0]==1 and H[1][1]==1 and H[2][2]== 1:
	flag = 1

if H[2][0]==1 and H[1][1]==1 and H[0][2]== 1:
	flag = 1

if flag == 1:
	print("Yes")
else:
	print("No")
#A[2][1] = 10
#print(A)
#print(flag)