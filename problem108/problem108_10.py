N=int(input())
k=N%1000
if k==0:
  t=0
else:
  t=1000-k
print(t)