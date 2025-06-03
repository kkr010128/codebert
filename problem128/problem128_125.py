X,N = map(int,input().split())
p = list(map(int,input().split()))

if not X in p:
    print(X)
else:
    for i in range(100):
        if not (X-i) in p:
            print(X-i)
            break
        elif not (X+i) in p:
            print(X+i)
            break




