n = int(input())
A = input()
A = A.split()
A = [int(i) for i in A]
A = sorted(A, reverse = True)
#print(A)
ans = 0

for i in range(int(n/2)):
	ans += A[i]*2

ans -= A[0]
#print(ans)
if n&1:
  ans += A[int(n/2)]


print(ans)