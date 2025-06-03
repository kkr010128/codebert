n,k=map(int,input().split())
a=0
for i in range(k,n+2):
    l=(i-1)*i//2
    r=(n-i+1+n)*i//2
    a+=(r-l+1)
    a%=10**9+7
print(a)