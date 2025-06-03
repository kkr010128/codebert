def resolve():
    L = list(map(int, input().split()))
    print("Yes" if len(L)-1 == len(set(L)) else "No")

if '__main__' == __name__:
    resolve()