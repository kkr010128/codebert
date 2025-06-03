n,*l=map(int,open(0).read().split())
a=t=0
for i in l:
  if i>t: t=i
  a+=t-i
print(a)