X, K, D = map(int, input().split())

X = abs(X)

if K - (X // D) < 0:
        X -= K * D
        print(X)
else:
        K = K - (X // D)
        X -= D * (X // D)
        if K % 2 == 0:
                print(abs(X))
        else:
                print(abs(X-D))