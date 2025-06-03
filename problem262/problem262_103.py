n=int(input())
s=[]
for i in range(n):
  a=int(input())
  t=[]
  for j in range(a):
    x=list(map(int,input().split()))
    t.append(x)
  s.append(t)

ans=0
for r in range(2**n):
  ans1=0
  za=[0 for i in range(n)]
  for w in range(n):
    if (r>>w)&1:
      ans1+=1
      za[w]+=1
  ch=0
  for h in range(n):
    if za[h]==1:
      for p in s[h]:
        A=p[0]-1
        B=p[1]
        if za[A]!=B:
          ch+=1
  if ch==0:
    ans=max(ans,ans1)
    
print(ans)