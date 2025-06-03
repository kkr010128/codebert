# https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_c

N, K = map(int, input().split())
A = list(map(int, input().split()))

while K > 0:
    K -= 1
    # imos法 (B)
    B = [0] * (N + 1)
    for i in range(N):
        l = max(0, i - A[i])
        r = min(N - 1, i + A[i])
        B[l] += 1
        if r + 1 < N:
            B[r + 1] -= 1

    C = 0
    for j in range(N):
        C += B[j]
        A[j] = C

    if set(A) == set([N]):
        break

print(*A)