(X,N) = map(int,input().split())
if N == 0:
    print(X)
else:
    p = list(map(int,input().split()))
    for i in range(N+1):
        if (X - i) not in p:
            print(X-i)
            break
        elif(X+i) not in p:
            print(X+i)
            break