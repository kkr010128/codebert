I=input
r=range
a=[[[0 for i in r(10)]for j in r(3)]for k in r(4)]
for i in r(int(I())):b,f,r,v=map(int,I().split());a[b-1][f-1][r-1]+=v
f=0
for i in a:
  if f:print('#'*20)
  else:f=1
  for j in i:print('',*j)