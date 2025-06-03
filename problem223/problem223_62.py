n,k=map(int,input().split())
p=list(map(int,input().split()))
ans=sum(p[0:k])+k
s=sum(p[0:k])+k
for i in range(1,n-k+1):
    s+=-p[i-1]+p[i+k-1]
    if ans<s:
        ans=s
print(ans/2)