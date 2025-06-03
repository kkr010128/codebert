n=int(input())
arr=list(map(int,input().split()))
if n==0:
  if arr[0]==1:
    print(1)
  else:
    print(-1)
  exit()
acum=[arr[0]]
for i in range(1,n+1):
  acum.append(acum[-1]+arr[i])
b=[0]*n
b[0]=1-arr[0]
b[0]=min(b[0],acum[n]-acum[0])
for i in range(1,n):
  b[i]=2*b[i-1]-arr[i]
  b[i]=min(b[i],acum[n]-acum[i])
for i in range(n):
  if b[i]<=0:
    print(-1)
    exit()
  if b[i]<=30 and arr[i+1]>2**b[i]:
    print(-1)
    exit()
ans=sum(arr)+sum(b)
print(ans)