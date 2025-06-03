N=int(input())
A=list(map(int, input().split()))
A.sort()
if N==1:
  print('YES')
  exit()
for i in range(N-1):
  if A[i]==A[i+1]:
    print('NO')
    exit()
else:
  print('YES')