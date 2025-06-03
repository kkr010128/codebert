X,N = map(int,input().split())
P = list(map(int,input().split()))
if X not in P:
    print(X)
else:
    d = 1
    while True:
        if X-d not in P:
            print(X-d)
            break
        if X+d not in P:
            print(X+d)
            break
        d += 1