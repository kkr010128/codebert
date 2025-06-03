k,n=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
dm=0
for i in range(n):
    dis=(a[i]-a[i-1])%k
    dm=max(dm,dis)
print(k-dm)
