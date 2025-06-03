n,m=map(int,input().split())
AClst=[0]*n
WAlst=[0]*n
AC=0
WA=0
for i in range(m):
  res = input().rstrip().split(' ')
  no=int(res[0])
  ans=str(res[1])
  if AClst[no-1]==0 and ans=="WA":
    WAlst[no-1]+=1
  elif AClst[no-1]==0 and ans=="AC":
    AClst[no-1]=1
for j in range(n):
  if AClst[j]==0 and WAlst[j]>0:
    WAlst[j]=0
  AC+=AClst[j]
  WA+=WAlst[j]
print(AC, WA)