N=int(input())
A=list(map(int,input().split()))

s=sum(A)

ans=1
eda=1

if N==0:
  if A[0]==1:
    print(1)
  else:
    print(-1)
  exit()

if A[0]!=0:
  print(-1)
  exit()
  
for i in range(1,N+1):
  if eda*2<=s:
    eda*=2
  else:
    eda=s
  ans+=eda
  eda-=A[i]
  s-=A[i]
  if eda<=0 and i != N:
    print(-1)
    exit()
if eda!=0:
  print(-1)
  exit()
print(ans)