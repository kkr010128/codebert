import itertools
N, M, Q = map(int,input().split())
ans = 0
A = []
B = []
C = []
D = []
for _ in range(Q):
    a, b, c, d = map(int,input().split())
    A.append(a-1)
    B.append(b-1)
    C.append(c)
    D.append(d)

ans = 0
for seq in itertools.combinations_with_replacement(range(M),N):
    tmp = 0
    for i in range(Q):
        if seq[B[i]] - seq[A[i]] == C[i]:
            tmp += D[i]
    ans = max(ans,tmp)

print(ans)