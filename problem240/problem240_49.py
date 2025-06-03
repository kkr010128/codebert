n,m=map(int,input().split())
ps=[list(input().split()) for _ in range(m)]
wa=[0]*n
w=0
ac=0
d=[0]*n
for p,s in ps:
  if s=='WA':
    if d[int(p)-1]==0:
      wa[int(p)-1]+=1
  else:
    if d[int(p)-1]==0:
      ac+=1
      d[int(p)-1]=1
      w+=wa[int(p)-1]
print(ac,w)