N = int(input())
A = [int(i) for i in input().split()]

l = sum(A)
ans = float("inf")
t = 0

for i in range(N-1):
	t += A[i]
	ans = min(ans,abs(l-2*t))
	#print("t,ans",t,ans)

print(ans)


