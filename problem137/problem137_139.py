n = int(input())
A = []
B = []
for i in range(n):
  a,b = list(map(int, input().split()))
  A.append(a)
  B.append(b)
A.sort()
B.sort()
j = n//2
if n%2 == 0:
  print((B[j]+B[j-1])-(A[j]+A[j-1])+1)
else:
  print(B[j]-A[j]+1)