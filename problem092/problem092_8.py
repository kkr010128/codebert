X,K,D = map(int, input().split())

if X<0:
    X = -X
if X - K*D >= 0:
    print(X-K*D)
else:
    i = 0
    while True:
        i+=1
        X -= D
        if X < 0:
            break
    if (K-i) % 2 == 0:
        print(abs(X))
    else:
        print(D-abs(X))

