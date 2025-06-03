X, N = map(int, input().split())
if N:
    lst = list(map(int, input().split()))

    for i in range(100):
        if X-i not in lst:
            print(X-i)
            break

        if X+i not in lst:
            print(X+i)
            break

else:
    print(X)