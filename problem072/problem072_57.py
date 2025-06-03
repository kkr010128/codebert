n=int(input())
alist=[0]*n
for i in range(n):
  a,b=map(int, input().split())
  if a==b:
      alist[i]=alist[max(i-1,0)]+1
if max(alist)>=3:
  print('Yes')
else:
  print('No')
