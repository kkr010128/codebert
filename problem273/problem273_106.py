from collections import defaultdict
N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
S = [0] * (N+1)
T = [0] * (N+1)
for i in range(N):
    S[i+1] = (S[i] + A[i])%K
    T[i+1] = (S[i+1] - (i+1))%K
rest = defaultdict(int)
for i in range(N+1):
    if i < K:
        ans += rest[T[i]]
        rest[T[i]] += 1
    else:
        rest[T[i-K]] -= 1
        ans += rest[T[i]]
        rest[T[i]] += 1
print(ans)