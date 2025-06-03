from collections import Counter
N = int(input())
P = []
Q = []
for L in range(1, N+1):
    L = str(L)
    a = int(L[0])
    b = int(L[-1])
    if a == 0 or b == 0:
        continue
    P.append((a, b))
C = Counter(P)

ans = 0
for i in range(len(P)):
    q = (P[i][-1], P[i][0])
    ans += C[q]

print(ans)