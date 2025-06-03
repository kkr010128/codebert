n,d,a=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
arr=sorted(arr,key=lambda x:x[0])
lim=[0]*n
pos=0
for i in range(n):
  while pos!=n-1:
    if arr[i][0]+2*d>=arr[pos+1][0]:
      pos+=1
    else:
      break
  lim[i]=pos
ans=0
damage=[0]*n
acum=0
pos=0
for i in range(n):
  while i>lim[pos]:
    acum-=damage[pos]
    pos+=1
    if pos==n:
      break
  ans+=max(0,(arr[i][1]-acum+(a-1))//a)
  damage[i]=a*max(0,(arr[i][1]-acum+(a-1))//a)
  acum+=damage[i]
print(ans)