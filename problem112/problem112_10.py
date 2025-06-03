M=10**9+7
n,k,*l=map(int,open(0).read().split())
lp,lm=[],[]
for i in l:
  if i<0: lm+=[i]
  else: lp+=[i]
cp,cm=len(lp),len(lm)
ok=0
if cp>0:
  if n==k: ok=1-cm%2
  else: ok=1
else: ok=1-k%2
a=1
if ok<1:
  l.sort(key=lambda x:abs(x))
  for i in range(k):
    a=a*l[i]%M
else:
  lp.sort()
  lm.sort(reverse=1)
  if k%2:
    a=lp.pop()
  p=[]
  while len(lp)>1:
    p+=[lp.pop()*lp.pop()]
  while len(lm)>1:
    p+=[lm.pop()*lm.pop()]
  p.sort(reverse=1)
  for i in range(k//2):
    a=a*p[i]%M
print(a)