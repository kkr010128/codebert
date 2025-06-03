n,m=map(int,input().split())
h=list(map(int,input().split()))
a=[0 for i in range(m)]
b=[0 for i in range(m)]
for i in range(m):
  a[i],b[i]=map(int,input().split())

count=0
c=[[] for i in range(n)]
for i in range(m):
  c[a[i]-1].append(b[i]-1)
  c[b[i]-1].append(a[i]-1)
  
for i in range(n):
  max_h=0
  for j in range(len(c[i])):
    max_h=max(max_h, h[c[i][j]])
  if max_h < h[i]:
    count+=1
print(count)