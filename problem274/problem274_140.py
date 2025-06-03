n,m=map(int,input().split())
s=input()
ans=[]
cursor=n
actualfail=0
while cursor!=0:
  if cursor<=m:
    ans.append(cursor)
    break
  failflag=1
  for i in range(m):
    if s[cursor-m+i]=='0':
      failflag=0
      ans.append(m-i)
      cursor-=m-i
      break
  if failflag==1:
    actualfail=1
    break
if actualfail==1:
  print(-1)
else:
  ans.reverse()
  for i in ans:
    print(i)