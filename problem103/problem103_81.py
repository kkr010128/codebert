n=int(input())
list=[[0]*n]
list=input().split()
for i in range(n):
  list[i]=int(list[i])

yen=1000
stock=0
keikou=0
for i in range(1,n):
  if list[i]-list[i-1]<=0:
    keikou+=1
if keikou!=n-1:
  for t in range(1,n):
    if list[t]-list[t-1]>=0:
      stock+=int(yen/list[t-1])
      yen-=list[t-1]*int(yen/list[t-1])
      yen+=list[t]*stock
      stock=0
print(yen)