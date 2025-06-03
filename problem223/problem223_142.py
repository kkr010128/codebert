N, K = map(int, input().split())
p = list(map(int, input().split()))
s = sum(p[:K])
m = s
for i in range(1, N-K+1):
    s = s - p[i-1] + p[i+K-1]
    m = max(m, s)
print((m+K)/2)
