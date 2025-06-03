import itertools
n,m,x=[int(x) for x in input().split()]
book=[]
for i in range(n):
  b=[int(x) for x in input().split()]
  book.append(b)
 
l=[]
a=itertools.product(range(2),repeat=n)
for i in a:
  l.append(i)
 
price=[]
for i in range(2**n):
  check_list=[0]*(m+1)
  for j in range(n):
    if l[i][j]==1:
      for k in range(m+1):
        check_list[k]+=book[j][k]
  check=[]
  for p in range(1,m+1):
    if check_list[p]<x:
      check.append(False)
  if check==[]:
    price.append(check_list[0])
 
if price==[]:
  print("-1")
else:
  print(min(price))