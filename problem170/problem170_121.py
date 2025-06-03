n,k=map(int,(input().split()))
ans=0
max=sum(range(n-k+1,n+1))*(n-k+2)
min=sum(range(k))*(n-k+2)
for i in range(1,n-k+2):
    min+=(k-1+i)*(n-k+2-i)
for i in range(1,n-k+2):
    max+=(n-k+1-i)*(n-k+2-i)
ans=(max-min+n-k+2)%(10**9+7)
print(ans)