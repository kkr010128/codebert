X, K, D = map(int, input().split())
X = abs(X)
if X - K*D >= 0:
    print(X - K*D)
else:
    M = X // D
    K -= M
    X -= M*D

    if K % 2:
        X -= D
    print(abs(X))
