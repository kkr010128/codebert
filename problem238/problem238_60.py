N, K, S = map(int, input().split(" "))
ans = []
for i in range(K):
    ans.append(S)

for i in range(N - K):
    ans.append(10 ** 9 if S != 10 ** 9 else 1)

print(' '.join([str(a) for a in ans]))