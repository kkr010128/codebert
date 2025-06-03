n,k,*a=map(int,open(0).read().split())
for i in range(n-k):print("Yes" if a[i]<a[i+k] else "No")