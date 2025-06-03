def resolve():
    X = list(map(int, input().split()))
    print(X.index(0)+1)

if '__main__' == __name__:
    resolve()