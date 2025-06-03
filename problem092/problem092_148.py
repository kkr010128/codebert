X, K, D = map(int,input().split())
X = abs(X)

if X > K*D:
    print( X - K*D )
else:
    a = X//D
    K -= a
    X -= D*a
    if K%2 == 0:
        print(X)
    else:
        print(abs(X-D))