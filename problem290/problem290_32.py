import sys
N,K=map(int,input().split())
alist=list(map(int,input().split()))
flist=list(map(int,input().split()))
alist.sort()
flist.sort(reverse=True)
#print(alist)
#print(flist)

def check(m):
  cnt=0
  for i in range(N):
    if alist[i]*flist[i]>m:
      cnt+=-(-(alist[i]*flist[i]-m)//flist[i])
  
  #print(m,cnt,K)
  if cnt<=K:
    return True
  else:
    return False

if sum(alist)<=K:
  print(0)
  sys.exit(0)

baseline=0
for i in range(N):
  baseline=max(baseline,alist[i]*flist[i])
#print(baseline)

l,r=0,baseline
while l<=r:
  mid=(l+r)//2
  #print(l,mid,r)
  if not check(mid-1) and check(mid):
    print(mid)
    break
  elif not check(mid):
    l=mid+1
  else:
    r=mid-1