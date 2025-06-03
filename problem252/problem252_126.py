from itertools import accumulate

MAX = 2 * 10 ** 5 + 5

N, M, *A = map(int, open(0).read().split())

B = [0] * MAX
for a in A:
    B[a] += 1

C = list(accumulate(reversed(B)))[::-1]

ng, ok = 1, MAX
while abs(ok - ng) > 1:
    m = (ok + ng) // 2
    if sum(C[max(0, m - a)] for a in A) >= M:
        ng = m
    else:
        ok = m

D = list(accumulate(reversed(list(i * b for i, b in enumerate(B)))))[::-1]
print(sum(D[max(0, ng - a)] - (ng - a) * C[max(0, ng - a)] for a in A) + ng * M)