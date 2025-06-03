N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
count = 0

for i in range(N-1):
  if A[i] == A[i+1]:
    count += 1
  i += 1

if count > 0:
  print('NO')
if count == 0:
  print('YES')