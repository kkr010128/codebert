N,M=map(int,input().split())
A=list(map(int,input().split()))
s=sum(A)
A.sort(reverse=True)
t=0
for x in range(M):
  if A[x]*4*M<s:
    t=1
    break
if t==0:
  print("Yes")
else:
  print("No")