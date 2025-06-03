X, K, D = map(int, input().split())

X = abs(X)

if X // D >= K:
    print(X - D*K)
else:
    e = X // D
    K -= e
    X -= D*e

    if K % 2 == 1:
        X = abs(X-D)

    print(X)
