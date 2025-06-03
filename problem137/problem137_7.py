def resolve():
	N = int(input())
	# set A and B arrays.
	A = []
	B = []
	for _ in range(N):
		A_i, B_i = map(int, input().split())
		A.append(A_i)
		B.append(B_i)
	# count median
	if N%2==1: # odd
		i = int((N-1)/2)
		median_min = sorted(A)[i]
		median_max = sorted(B)[i]
	else:
		i_0 = int((N/2)-1)
		i_1 = int(N/2)
		ordered_A = sorted(A)
		ordered_B = sorted(B)
		median_min = ordered_A[i_0] + ordered_A[i_1] # 2 times of median of A
		median_max = ordered_B[i_0] + ordered_B[i_1]
	print(median_max - median_min +1)
    
resolve()