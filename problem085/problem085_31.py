n,*a=map(int,open(0).read().split())
m=6**8
c=[0]*m
p=[1,1]+c[:]
for i in range(m):
  if p[i]<1:
    for j in range(i,m,i):p[j]=i
for a in a:
  s={a}
  while a!=p[a]:
    s|={p[a]}
    a//=p[a]
    s|={a}
  for i in s:c[i]+=1
print(('not','psaeitr'[max(c[2:])>1::2]+'wise')[max(c[2:])<n],'coprime')