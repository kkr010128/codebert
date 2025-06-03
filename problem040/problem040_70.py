A = list(map(int,input().split(" ")))
num = len(A)

for i in range(1,num):
	v = A[i]

	for j in range(i-1,-1,-1):
		if A[j] > v:
			#値移動
			A[j+1] = A[j]
		else:
			#何もしない
			A[j+1] = v
			break
	else:
		A[0] = v

list2 = [str(k) for k in A]
print(" ".join(list2))

