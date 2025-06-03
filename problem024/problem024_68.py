n,k=map(int,input().split())
w=[int(input()) for i in range(n)]
def ok(p):
  t=[0]*k
  curr=0
  for i in w:
    if i>p:
      return False
    if t[curr]+i>p:
      curr+=1
      if curr>=k:
        return False
    t[curr]+=i
  return True
l=0
h=10**9+1
while True:
  if l>=h:
    print(l)
    break
  if h==l+1:
    print(l if ok(l) else h)
    break
  mid=(l+h)//2
  if ok(mid):
    h=mid
  else:
    l=mid

