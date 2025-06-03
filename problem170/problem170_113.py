n,k=map(int,input().split())
ans=0
max=0
min=0
for i in range(k,n+1):
    ans+=i*(n-i+1)+1
    ans%=1000000007
print(ans+1)