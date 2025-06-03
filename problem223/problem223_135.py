N,K = map(int,input().split())
p = list(map(int,input().split()))

l = []
for i in range(N):
    l.append(((1+p[i])*(p[i]/2))/p[i])

que = [0]*(N+1)
for i in range(1,N+1):
    que[i] = l[i-1]+que[i-1]

ans = 0
for i in range(K,len(l)):
    ans = max(ans,que[i+1]-que[i+1-K])

if N == K:
    print(max(que))
else:
    print(ans)