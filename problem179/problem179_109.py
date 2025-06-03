n,m=map(int,input().split())
A = list(map(int,input().split()))
A.sort()
A = A[::-1]
for i in range(m):
  if A[i]*4*m < sum(A):
    print("No")
    break
else:
  print("Yes")