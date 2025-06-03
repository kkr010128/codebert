import sys
N = int(input())
A = [int(x) for x in input().split()]

L = [0] * N + [A[N]]    # 下限
U = [0] * N + [A[N]]    # 上限
for i in range(N - 1, -1, -1):
    L[i] = (L[i + 1] + 1) // 2 + A[i]
    U[i] = U[i + 1] + A[i]

if 1 < L[0]:
    print(-1)
    sys.exit()

U[0] = 1
for i in range(1, N + 1):
    U[i] = min(2 * (U[i - 1] - A[i - 1]), U[i])   # 深さiの頂点数

print(sum(U))