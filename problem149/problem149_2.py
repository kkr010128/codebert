N, M, X = map(int, input().split())
C = []
A = []
for _ in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)
ans = 10**18
for s in range(1<<N):
    an = 0
    L = [0] * M
    for i, (c, a) in enumerate(zip(C, A)):
        if s>>i&1:
            an += c
            for j, a_ in enumerate(a):
                L[j] += a_
    if all(l >= X for l in L):
        if an < ans:
            ans = an
if ans == 10**18:
    print(-1)
else:
    print(ans)
