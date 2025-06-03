N, K, S = map(int, input().split())
a = [S for i in range(K)]
if S == 10 ** 9:
    S -= 2
for i in range(N - K):
    a.append(S + 1)
print(*a)
