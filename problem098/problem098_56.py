n=int(input())
c=list(input())
r=[]
w=[]
for i in range(n):
  if c[i]=='R':
    r.append(i)
  else:
    w.append(i)
r.reverse()
ans=0
for i in range(min(len(r),len(w))):
  if r[i]>w[i]:
    ans+=1
print(ans)