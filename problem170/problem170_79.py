n,k=map(int,input().split())
d=0
for i in range(k,n+2):
    b=i*(i-1)/2
    c=i*(2*n-i+1)/2
    d+=(c-b+1)
print(int(d)%(10**9+7))