k=int(input())
A=[0]*k
f=0
for i in range(k):
  if i==0:
    A[i]=7%k
  else:
    A[i]=(10*A[i-1]+7)%k
  
  if A[i]==0:
    f=1
    print(i+1)
    exit()
if not f:
  print(-1)