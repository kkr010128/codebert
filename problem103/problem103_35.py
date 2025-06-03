# WA

N = int(input())
A = [int(_) for _ in input().split()]

dp = [1000]
K = [0]
C = [0]

for i in range(N):
    k, c = divmod(dp[-1], A[i])
    v = dp[-1]
    for j in range(i+1):
        u = K[j] * A[i] + C[j]
        v = max(u, v)
    K.append(k)
    C.append(c)
    dp.append(v)
print(dp[-1])
