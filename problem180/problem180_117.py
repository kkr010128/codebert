n,k=map(int,input().split())
s=n//k
m=min((n-s*k),((s+1)*k-n))
print(m)