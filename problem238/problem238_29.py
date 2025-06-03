N, K, S = map(int, input().split())
ans = []
n = N-K
for i in range(K):
  ans.append(S)
for i in range(n):
  if S == 10**9:
    ans.append(S-1)
  else:
    ans.append(S+1)
ans=[str(a) for a in ans]
ans=" ".join(ans)

print(ans)