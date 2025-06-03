N, K = [int(_) for _ in input().split()]
P = [int(_) - 1 for _ in input().split()]
C = [int(_) for _ in input().split()]

def f(v, K):
    if K == 0:
        return 0
    if max(v) < 0:
        return max(v)

    n = len(v)
    X = [0]
    for i in range(n):
        X.append(X[-1] + v[i])

    ans = -(10 ** 10)
    for i in range(n + 1):
        for j in range(i):
            if i - j > K:
                continue
            ans = max(ans, X[i] - X[j])
    return(ans)

X = [False for _ in range(N)]
ans = -(10 ** 10)

for i in range(N):
    if X[i]:
        continue
    t = i
    v = []
    while X[t] is False:
        X[t] = True
        v.append(C[t])
        t = P[t]

    n = len(v)
    if K > n:
        s = sum(v)
        x = f(v * 2, n)
        if s > 0:
            a = s * (K // n - 1) + max(s + f(v * 2, K % n), x)
        else:
            a = x
    else:
        a = f(v * 2, K)
    ans = max(a, ans)

print(ans)
