n = int(input())
A = list(map(int, input().split()))

a=0
result=0

for i in range(n-1):
  if A[i] > A[i+1]:
    a = A[i] - A[i+1]
    A[i+1] += a
    result += a
    
print(result)