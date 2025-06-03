X,K,D = map(int,input().split())
X = abs(X)
a = int(X/D)
if a < K:
        K -= a
        X -= a*D

if K*D <= X:
    X -= K*D
else:
    K %= 2
    for i in range(K):
        if X > 0:
            X -= D
        else:
            X += D
print(abs(X))