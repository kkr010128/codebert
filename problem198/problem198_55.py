from copy import copy
n=int(input())
alpha="abcdefghij"
c=[0 for i in range(n)]
m=[0 for i in range(n)]
ans=[]
ans.append(copy(c))
while True:
  c[-1]+=1
  i=n-1
  while i!=0 and c[i]-2==m[i-1]:
    c[i]=0
    i-=1
    c[i]+=1
  if i==0:
    break
  for i in range(1,n):
    m[i]=max(m[i-1],c[i])
  ans.append(copy(c))
for i in ans:
  print("".join(map(lambda x:alpha[x],i)))