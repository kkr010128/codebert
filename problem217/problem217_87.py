N=int(input())
A=list(map(int, input().split()))

flag = 1
for i in range(len(A)):
  if A[i] % 2 == 0:
    if A[i] % 3 != 0 and A[i] % 5 != 0:
      flag = 0
      break
print(['DENIED', 'APPROVED'][flag])