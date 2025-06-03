n = int(input())
A = list(map(int,input().split()))
smallest = A[0]
ans = 0
for x in range(len(A)-1):
	if A[x] > A[x+1]:
		ans += A[x] - A[x+1] 
		A[x+1] = A[x]

print(ans)

		

