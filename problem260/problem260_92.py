def resolve():
    A = sum(map(int, input().split()))
    print("bust" if A >= 22 else "win")

if '__main__' == __name__:
    resolve()