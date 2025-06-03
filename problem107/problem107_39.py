def g(x):
  S=format(x,"22b")
  cnt=0
  for i in range(20):
    if S[-1-i]=="1":
      cnt=cnt+1
  return x%cnt

n=int(input())
X=input()
a=0
for i in range(n):
  if X[i]=="1":
    a=a+1
#最初に割るのは a-1 or a+1 -> a==0,1 に注意
if a==0:
  for i in range(n):
    print(1)
  exit()
if a==1:
  if X[-1]=="1":
    for i in range(n-1):
      print(2)
    print(0)
    exit()
  else:
    for i in range(n-1):
      if X[i]=="1":
        print(0)
      else:
        print(1)
    print(2)
    exit()
D=[0]*n
E=[0]*n
D[0]=1%(a-1)
E[0]=1%(a+1)
b=int(X[-1])%(a-1)
c=int(X[-1])%(a+1)
for i in range(n-1):
  D[i+1]=(D[i]*2)%(a-1)
  E[i+1]=(E[i]*2)%(a+1)
  if X[-2-i]=="1":
    b=(b+D[i+1])%(a-1)
    c=(c+E[i+1])%(a+1)
for i in range(n):
  if X[i]=="1":
    x=(b+a-1-D[-1-i])%(a-1)
    ans=1
    while x!=0:
      x=g(x)
      ans=ans+1
    print(ans)
  else:
    x=(c+E[-1-i])%(a+1)
    ans=1
    while x!=0:
      x=g(x)
      ans=ans+1
    print(ans)