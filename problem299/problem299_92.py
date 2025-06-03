n,*a=map(int,open(0).read().split())
b=[0]*n
for i in range(n):
    b[a[i]-1]=str(i+1)
print(' '.join(b))