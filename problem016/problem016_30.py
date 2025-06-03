num = int(input())
A = input().split(" ")
B = A.copy()

#bubble sort
for i in range(num):
	for j in range(num-1,i,-1):
		#英字ではなく、数字で比較する
		m1 = int(A[j][1:])
		m2 = int(A[j-1][1:])
		if m1 < m2:
			A[j],A[j-1] = A[j-1],A[j]

print(*A)
print("Stable")

#selection sort
for i in range(num):
	minv = i
	for j in range(i+1,num):
		m1 = int(B[minv][1:])
		m2 = int(B[j][1:])
		if m1 > m2:
			minv = j
	B[i],B[minv] = B[minv],B[i]

print(*B)
if A == B:
	print("Stable")
else:
	print("Not stable")


