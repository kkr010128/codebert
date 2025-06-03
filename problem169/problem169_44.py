n=int(input())
a=list(map(int,input().split()))
d={}
for v in a:
  if v not in d:
    d[v]=0
  d[v]+=1
  
for x in range(n):
  if x+1 not in d:
    print(0)
  else:
    print(d[x+1])