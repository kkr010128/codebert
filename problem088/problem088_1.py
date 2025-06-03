N = int(input())
A = [0]*N
A = list(map(int, input().split()))
 
sum_step = 0
 
for n in range(1,N):
  if A[n] < A[n-1]:
    sum_step += A[n-1] - A[n]
    A[n] = A[n-1]

print(sum_step)