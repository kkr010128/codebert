N,M=map(int,input().split())
if N == 1:begin,end=0,10
elif N==2:begin,end=10,100
else: begin,end=100,1000
ans = -1
SC=[]
for i in range(M):
  s,c = map(int,input().split())
  SC.append((s,c))
for n in range(begin,end):
  count = 0
  n = str(n)
  for i in range(M):
    if int(n[SC[i][0]-1])==SC[i][1]:count+=1
  if count==M:
    ans=n
    break
print(ans)