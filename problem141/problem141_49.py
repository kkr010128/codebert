import sys
N=int(input())
alist=list(map(int,input().split()))

if N==0 and alist[0]!=1:
  print(-1)
  sys.exit(0)
elif N>0 and alist[0]>0:
  print(-1)
  sys.exit(0)

#pow2d=1<<N
blist=[0]*(N+1)
for d in reversed(range(1,N+1)):
  if d>50:
    blist[d-1]=alist[d]+blist[d]
  else:
    blist[d-1]=min(alist[d]+blist[d],(1<<(d-1))-alist[d-1])
  if blist[d-1]<0:
    print(-1)
    sys.exit(0)
  #pow2d>>=1
  
#print(alist,blist)
cmax_bu=[0]*(N+1)
for d in range(N+1):
  cmax_bu[d]=alist[d]+blist[d]
#print(cmax_bu)

pow2d=1
blist=[0]*(N+1)
if alist[0]==0:
  blist[0]=1
for d in range(1,N+1):
  if pow2d<10**10:
    pow2d<<=1
    c=min(2*blist[d-1],pow2d,cmax_bu[d])
  else:
    c=min(2*blist[d-1],cmax_bu[d])
  blist[d]=c-alist[d]
  if blist[d]<0:
    print(-1)
    sys.exit(0)
#print(alist,blist)

answer=0
for i in range(N+1):
  answer+=alist[i]+blist[i]
  
print(answer)