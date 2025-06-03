h,w,m=map(int,input().split())

H,W=[0]*h,[0]*w
P=set()

for i in range(m):
  y,x=map(int,input().split())
  H[~-y]+=1
  W[~-x]+=1
  P.add(~-y*w+~-x)

mh,mw=max(H),max(W)
MH=[i for i,h in enumerate(H) if h==mh]
MW=[i for i,v in enumerate(W) if v==mw]
for y in MH:
  for x in MW:
    if y*w+x not in P:
      print(mh+mw)
      exit()

print(mh+mw-1)
