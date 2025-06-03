N,K = map(int,input().split())

M = list(map(int,input().split()))
M =sorted(M,reverse=True)

print(sum(M[K:]))