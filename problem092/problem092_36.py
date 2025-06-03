X, K, D = map(int, input().split())
X = abs(X)

ans = 0
if X // D > K:
    ans = X - D*K
else:
    e = X // D
    K -= e
    X -= D * e
    if K % 2 == 1: X = abs(X-D)
    ans = X

print(ans)