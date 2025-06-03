N = int(input())

A = [0]*N
B = [0]*N

for i in range(N):
  A[i],B[i] = map(int, input().split())
A.sort()
B.sort()
 
if len(A)%2 != 0:
  ans = B[N//2]-A[N//2]+1
else:
  ans = (B[N//2]+B[N//2-1]) - (A[N//2]+A[N//2-1]) + 1

print(ans)