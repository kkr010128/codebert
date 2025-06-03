n,m=map(int,input().split())
s=input()[::-1]

if "1"*m in s:
  print(-1)
  exit(0)

ans=[]
cur=0
while cur<len(s):
  for j in range(m,0,-1):
    if cur+j>=len(s):
      continue
    if s[cur+j]=="0":
      cur=cur+j
      ans.append(j)
      break
  if cur==len(s)-1:
    break

ans=ans[::-1]
print(*ans)