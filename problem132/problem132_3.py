import itertools
N, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
for _ in range(K):
    cumsum = [0] * (N + 2)
    for i, a in enumerate(A):
        i += 1
        cumsum[max(0, i - a)] += 1
        cumsum[min(i + a + 1, N + 1)] -= 1
    A = list(itertools.accumulate(cumsum))[1:N + 1]
    if min(A) == N:
        break
print(' '.join(map(str, A)))
