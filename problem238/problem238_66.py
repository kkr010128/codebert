N, K, S = map(int, input().split())
ans = [S] * K
 
if S != 10**9:
    for i in range(N-K):
        ans.append(S+1)
else:
    for j in range(N-K):
        ans.append(1)
 
print(" ".join([str(x) for x in ans]))