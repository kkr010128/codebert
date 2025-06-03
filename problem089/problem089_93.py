h,w,m=map(int,input().split())
hl=[0]*(h)
wl=[0]*(w)
bom=[]
for i in range(m):
  h1,w1=map(int,input().split())
  bom.append([h1-1,w1-1])
  hl[h1-1]+=1
  wl[w1-1]+=1

mh=max(hl)
mw=max(wl)
ans=mh+mw
mhl=set()
mwl=set()
for i in range(h):
  if mh==hl[i]:
    mhl.add(i)
    
for i in range(w):
  if mw==wl[i]:
    mwl.add(i)

count=len(mhl)*len(mwl)
for i in range(len(bom)):
  if bom[i][0] in mhl and bom[i][1] in mwl:
    count-=1
if count>0:
  print(ans)
else:
  print(ans-1)
