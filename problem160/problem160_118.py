from itertools import combinations_with_replacement as C

N, M, Q = map(int, input().split())

a = [0] * Q
b = [0] * Q 
c = [0] * Q 
d = [0] * Q
for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())

A_ = list(range(1, M + 1))
A_ = list(C(A_, N))

ans = 0
ans_ = 0
for A in A_:
    ans_ = 0
    for i in range(Q):
        if A[b[i] - 1] - A[a[i] - 1] == c[i]:
            ans_ += d[i]
    if ans < ans_:
        ans = ans_

print(ans)