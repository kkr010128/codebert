import sys
H,W,M=map(int,input().split())

hlist=[0]*H
wlist=[0]*W
hwset=set()
for _ in range(M):
  h,w=map(int,input().split())
  hlist[h-1]+=1
  wlist[w-1]+=1
  hwset.add((h-1,w-1))
  
hmax=max(hlist)
hlist2=[]
for i in range(H):
  if hlist[i]==hmax:
    hlist2.append(i)

wmax=max(wlist)
wlist2=[]
for i in range(W):
  if wlist[i]==wmax:
    wlist2.append(i)
#print(hlist2,wlist2)

H2=len(hlist2)
W2=len(wlist2)

if H2*W2>M:
  print(hmax+wmax)
else:
  for i in range(H2):
    ii=hlist2[i]
    for j in range(W2):
      jj=wlist2[j]
      if not (ii,jj) in hwset:
        print(hmax+wmax)
        sys.exit(0)
  else:
    print(hmax+wmax-1)