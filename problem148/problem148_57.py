def resolve():
    A, B, C, K = list(map(int, input().split()))
    print(min(A, K) - max(0, K-(A+B)))

if '__main__' == __name__:
    resolve()