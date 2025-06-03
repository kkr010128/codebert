N,K = map(int,input().split())
p = list(map(int,input().split()))
ans,num = sum(p[0:K]),sum(p[0:K])
for i in range(N-K):
    num = num + p[i+K] - p[i]
    ans = max(ans, num)
print((ans+K)/2)