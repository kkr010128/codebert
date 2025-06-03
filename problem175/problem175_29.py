from collections import Counter
N = int(input())
S = list(input())
cnt = Counter(S)
ans = 1
for s in list('RGB'):
    ans *= cnt[s]

for i in range(N):
    for j in range(i + 1, N):
        K = 2*j - i
        if K >= N:
            break
        if (S[i] != S[j]) & (S[j] != S[K]) & (S[i] != S[K]):
            ans -= 1
print(ans)
