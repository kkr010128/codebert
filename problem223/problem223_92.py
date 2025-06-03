N, K = list(map(int, input().split()))
P = list(map(int, input().split()))

s = 0

for i in range(K):
    s += P[i]

s_max = s

for i in range(N - K):
    s = s - P[i] + P[i+K]
    if s > s_max:
        s_max = s

print((s_max + K) / 2)