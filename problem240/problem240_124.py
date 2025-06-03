n,m=map(int,input().split())

l=[0]*n
w=0
c=0
ac=set()

for i in range(m):
  p,s=map(str,input().split())
  p=int(p)
  if s=='WA':
    l[p-1]+=1
  else:
    if p not in ac:
      c+=1
      w+=l[p-1]
      ac.add(p)

print(c,w)
