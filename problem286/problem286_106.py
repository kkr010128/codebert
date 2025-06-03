def resolve():
    A, B = list(map(int, input().split()))
    if A >= 10 or B >= 10:
        print(-1)
    else:
        print(A*B)

if '__main__' == __name__:
    resolve()