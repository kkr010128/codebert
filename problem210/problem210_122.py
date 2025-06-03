f=input
n,l,q=int(f()),list(f()),int(f())
B=[[0]*-~n for i in range(26)]
def S(o,i):
  s=0
  while i: s+=B[o][i]; i-=i&-i
  return s
def A(o,i,x):
  while i<=n: B[o][i]+=x; i+=i&-i
for i in range(n): A(ord(l[i])-97,i+1,1)
for i in range(q):
  a,b,c=f().split(); b=int(b)
  if a>'1': print(sum(1 for o in range(26) if S(o,int(c))-S(o,b-1)))
  else: A(ord(l[b-1])-97,b,-1); l[b-1]=c; A(ord(c)-97,b,1)