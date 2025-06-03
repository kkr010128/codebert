import sys

n,m=map(int,input().split())
ans=[0]*n

for i in range(m):
  s,c=map(int,input().split())
  s-=1
  if ans[s]!=0 and ans[s]!=c:
    print(-1)
    sys.exit()
    
  else:
    ans[s]=c
    
if n==3 and m==1 and ans==[0,0,0]:
  print(-1)
  sys.exit()
    
if n!=1 and ans[0]==0:
  ans[0]=1
    
for i in range(n):
  ans[i]=str(ans[i])
  
print("".join(ans))