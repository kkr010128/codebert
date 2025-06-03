N=int(input())
L=list(input() for i in range(N))
L=sorted(L)
X=L[0]
c=0
d=0
e=[]
for i in range(N):
  if L[i]==X:
    c+=1
    if i==N-1 and c>d:
      e=[X]
    elif i==N-1 and c==d:
      e.append(X)
  elif L[i]!=X and d<c:
    d=c
    c=0
    e=[]
    e.append(X)
    X=L[i]
    c+=1
  elif L[i]!=X and d==c:
    c=1
    e.append(X)
    X=L[i]
    if i==N-1:
      e.append(X)
  elif L[i]!=X and d>c:
    c=0
    X=L[i]
    c+=1
for i in e:
  print(i)