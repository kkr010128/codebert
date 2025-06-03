N,M=map(int,input().split())
sc=[]
for i in range(M):
  sc.append(list(map(int,input().split())))

ans=-1
cnt=10**(N-1)
if cnt==1:cnt-=1
while True:
  if len(str(cnt))>N:break
  if len(str(cnt))!=N:continue
  ret=True
  for i in range(M):
    if str(cnt)[sc[i][0]-1]!=str(sc[i][1]):
      ret=False
      break
  if ret:
    ans=cnt
    break
  cnt+=1
print(ans)