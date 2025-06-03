N, K, S = map(int, input().split())
ans = []
for _ in range(K):
    ans.append(S)

if S != 10**9:
    for _ in range(N-K):
        ans.append(S+1)
else:
    for _ in range(N-K):
        ans.append(S-1)

print(*ans)