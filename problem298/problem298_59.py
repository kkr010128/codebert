N, K = map(int, input().split())
h = list(map(int, input().split()))

cn = 0

for i in range(N):
    if h[i] >= K:
        cn = cn + 1
        
print(cn)
