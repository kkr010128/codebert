N, K, *A = map(int, open(0).read().split())

MOD = 10 ** 9 + 7
s = []  # v >= 0
t = []  # v < 0
for i in range(N):
    if A[i] < 0:
        t.append(A[i])
    else:
        s.append(A[i])
        
ok = False  # ans > 0
if len(s) > 0:
    if N == K:
        ok = len(t) % 2 == 0
    else:
        ok = True
else:
    ok = K % 2 == 0

ans = 1
if not ok:
    x = sorted(A, key=lambda x: abs(x))
    for i in range(K):
        ans = ans * x[i] % MOD
else:
    s.sort()
    t.sort(key=lambda x: abs(x))
    if K % 2 == 1:
        ans = ans * s.pop() % MOD
        
    p = []
    while len(s) >= 2:
        x = s.pop() * s.pop()
        p.append(x)
    
    while len(t) >= 2:
        x = t.pop() * t.pop()
        p.append(x)

    p.sort(reverse=True)
    for i in range(K // 2):
        ans = ans * p[i] % MOD
    
print(ans)

