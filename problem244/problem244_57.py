def resolve():
    K, X = list(map(int, input().split()))
    print("Yes" if 500*K>=X else "No")

if '__main__' == __name__:
    resolve()