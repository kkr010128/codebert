def resolve():
    X, Y = list(map(int, input().split()))
    for t in range(X+1):
        k = X - t
        if 2*t + 4*k == Y:
            print("Yes")
            return
    print("No")

if '__main__' == __name__:
    resolve()