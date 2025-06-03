N, K, S = map(int, input().split())
A = []
for i in range(K):
    A.append(S)

if S != 10 ** 9:
    res = S + 1
else:
    res = 1

for j in range(N - K):
    A.append(res)
print(*A)
