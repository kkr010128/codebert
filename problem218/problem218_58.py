c={}
N=int(input())
for i in range(N):
  s=input()
  if s not in c:
    c[s]=1
  else:
    c[s]+=1
n=max(c.values())
L=list()
for i in c:
  if c[i]==n:
    L.append(i)
L=sorted(L)
for i in L:
  print(i)