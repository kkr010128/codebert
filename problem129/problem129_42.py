M=10**6+1
_,*l=map(int,open(0).read().split())
a=[0]*M
for i in l:
  if a[i]<1:
    for j in range(i*2,M,i):
        a[j]=2
  a[i]+=1
print(a.count(1))