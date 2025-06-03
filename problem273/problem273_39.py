n,k,*a=map(int, open(0).read().split())
b=[0]*-~n
for i in range(n):b[i+1]=(a[i]+b[i]-1)%k
d={k:0}
a=0
for l,r in zip([k]*min(k,n+1)+b,b):d[l]-=1;t=d.get(r,0);a+=t;d[r]=t+1
print(a)