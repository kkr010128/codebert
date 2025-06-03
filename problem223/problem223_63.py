N,K=map(int,input().split())
p=list(map(int,input().split()))

res=0
s=sum(p[:K])
for i in range(N-K+1):
    res=max(res,(s+K)/2)
    if i!=N-K:
        s=s+p[i+K]-p[i]
print(res)