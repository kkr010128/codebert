N, K = map(int, input().split())
P = list(map(int, input().split()))

pos = 0
n = m = sum(P[0:K])
for i in range(1,N):
    if i+K > N:
        break
    n = n - P[i-1] + P[K-1+i]
    if n > m:
        pos = i
        m = n

print((sum(P[pos:pos+K]) + K) / 2)