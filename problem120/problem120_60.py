N,K = map(int,input().split())
P = list(map(int,input().split()))

P.sort()
ans = sum(P[0:K])

print(ans)