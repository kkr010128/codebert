N, K = list(map(int, input().split()))
RSP = list(map(int, input().split()))
D = {'r': 0, 's': 1, 'p': 2}
T = input()

M = N//K
dp = [[[0]*3 for _ in range(M+(i < (N % K)))] for i in range(K)]
# print(dp)


def wins(i, s):
    j = D[s]
    return i % 3 == (j-1) % 3


ans = 0
for i in range(K):
    L = dp[i]
    for k in range(3):
        L[0][k] = RSP[k]*wins(k, T[i])
    for j in range(1, len(L)):
        for k in range(3):
            L[j][k] = max(L[j-1][l] + RSP[k]*wins(k, T[i+j*K])
                          for l in range(3) if k != l)
    # print(L)
    ans += max(L[-1][k] for k in range(3))
print(ans)
