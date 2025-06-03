n=int(input())
arr=list(map(int,input().split()))
ans=sum(arr)
if n==0:
  if arr[0]==1:
    print(1)
  else:
    print(-1)
  exit()
for i in range(n):
  if i<=30 and arr[i]>=2**i:
    print(-1)
    exit()
if n<=30 and arr[n]>2**n:
  print(-1)
  exit()
maxs=[0]*(n+1)
maxs[0]=1
for i in range(1,n):
  maxs[i]=2*maxs[i-1]-arr[i]
tmp=arr[n]
for i in range(n-1,-1,-1):
  maxs[i]=min(maxs[i],tmp)
  tmp+=arr[i]
mins=[0]*(n+1)
for i in range(n-1,-1,-1):
  mins[i]=(mins[i+1]+arr[i+1]+1)//2
for i in range(n):
  if maxs[i]<mins[i]:
    print(-1)
    exit()
ans+=sum(maxs)
print(ans)