n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
s=[]
for i in range(n):
  if l[i][0]==l[i][1]:
    s.append(1)
  else:
    s.append(0)
g=[]
for i in range(n-2):
  g.append(s[i]*s[i+1]*s[i+2])
ok=0
for i in range(n-2):
  if g[i]==1:
    ok=1
    break
if ok==1:
  print("Yes")
else:
  print("No")
