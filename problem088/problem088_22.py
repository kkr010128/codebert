N = int(input())
A = list(map(int, input().split()))

sum = 0
for i in range(N-1):
	if A[i] >= A[i+1]:
		sum += A[i] - A[i+1]
		A[i+1] = A[i]
		
print(sum)
