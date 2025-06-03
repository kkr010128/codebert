def f(m):
    return (((N+1)*((m*(m+1))//2))%p-((m*(m+1)*(2*m+1))//6)%p+m%p)%p
p = 10**9+7
N,K = map(int,input().split())
cnt = (f(N+1)-f(K-1))%p
print(cnt)