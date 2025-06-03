h,n = map(int,input().split())
A= list(map(int,input().split()))
for i in range(n):
  h-= A[i]
if h>0:
  print("No")
else:
  print("Yes")