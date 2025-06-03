n=int(input())
a=list(sorted(map(int,input().split())))
d=[0 for i in range(a[-1]+1)]
c=0
for i in range(len(a)):
  if d[a[i]]:
    continue
  if i==len(a)-1 or a[i]!=a[i+1]:
    c+=1
  for j in range(a[i],a[-1]+1,a[i]):
    d[j]=1
print(c)