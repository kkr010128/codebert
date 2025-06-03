h,w=map(int,input().split())
s=[0]*h
t=[0]*h
for i in range(h):
  st=str(input())
  st=list(st)
  s[i]=st
  tt=[0]*w
  t[i]=tt
if s[0][0]=="#":
  t[0][0]=1
for i in range(1,h):
  t[i][0]=t[i-1][0]
  if s[i-1][0]=="." and s[i][0]=="#":
    t[i][0]=t[i-1][0]+1
for i in range(1,w):
  t[0][i]=t[0][i-1]
  if s[0][i-1]=="." and s[0][i]=="#":
    t[0][i]=t[0][i-1]+1
for i in range(1,w):
  for j in range(1,h):
    if s[j-1][i]=="." and s[j][i]=="#":
      t1=t[j-1][i]+1
    else:
      t1=t[j-1][i]
    if s[j][i-1]=="." and s[j][i]=="#":
      t2=t[j][i-1]+1
    else:
      t2=t[j][i-1]
    t[j][i]=min(t1,t2)
print(t[h-1][w-1])