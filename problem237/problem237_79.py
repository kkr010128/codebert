n=int(input())
lr=[]
for i in range(n):
  x,l=map(int,input().split())
  lr.append((x-l,x+l))
lr.sort(key=lambda x: x[1])
ans=0
l=-10**18
r=0
for i in range(n):
  if i==0:
    tl,tr=lr[i]
    l=tl
    r=tr
    ans+=1
    continue
  tl,tr=lr[i]
  if tl>=r:
    ans+=1
    r=tr
    l=tl
print(ans)



