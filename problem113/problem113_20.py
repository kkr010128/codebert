d=int(input()) #365
c=list(map(int,input().split()))
s=[]
for i in range(d):
  s.append(list(map(int,input().split())))

ll=[0 for i in range(26)]
l=[]
ans=[]
for i in range(d):
  for j in range(26):
    ll[j]+=1
  m=-(10**10)
  for j in range(26):
    t=s[i][j]+ll[j]*c[j]
    if m<t:
      m=t
      tt=j
  l.append(ll[tt])
  ans.append(tt)
  ll[tt]=0
print("\n".join(map(lambda x:str(x+1),ans)))