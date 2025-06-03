n,*A=map(int,open(0).read().split());m=1000
for x,y in zip(A,A[1:]):
  if x<y:m=m//x*y+m%x
print(m)