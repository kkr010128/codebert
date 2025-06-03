import sys
n,m=map(int,input().split())
if n==3:
  ans=["1","0","0"]
elif n==2:
  ans=["1","0"]
else:
  ans=["0"]
cnt=[0,0,0]
for i in range(m):
  s,c=map(int,input().split())
  if s==1 and c==0 and n!=1:
    print(-1)
    sys.exit()
  elif ans[s-1]!=str(c):
    if cnt[s-1]==0:
      ans[s-1]=str(c)
      cnt[s-1]=1
    else:
      print(-1)
      sys.exit()
print("".join(ans))


