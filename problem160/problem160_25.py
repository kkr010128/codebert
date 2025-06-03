from itertools import combinations_with_replacement as H
N, M, Q = map(int, input().split())
ans = 0
query = [list(map(int, input().split())) for _ in range(Q)]

for A in H(list(range(1, M+1)), N):
    acc = 0
    for j in range(Q):
        a, b, c, d = query[j]
        if A[b - 1] - A[a - 1] == c:
            acc += d
    ans = max(ans, acc)
print(ans)
