s=list(input())
top=bool()
t=[]
u=[]
n=int(input())
for i in range(n):
  q=list(map(str,input().split()))
  if q[0]=='1':
    top=not top
  else:
    if (q[1]=="1") ^ top:
      t.append(q[2])
    else:
      u.append(q[2])
s=list(reversed(t))+s+u
if top:
  print(*list(reversed(s)),sep='')
else:
  print(*s,sep='')