N = int(input())
A = list(map(int,input().split()))

Money = 1000
Stock = 0
for i in range(N-1):
	if A[i] < A[i+1]:
		Stock = Stock + (Money//A[i])
		Money = Money % A[i]
	elif A[i] > A[i+1]:
		Money = Money + Stock * A[i]
		Stock = 0

ans = Money + Stock * A[i+1]
print(ans)