def resolve():
    H, A = list(map(int, input().split()))
    import math
    print(math.ceil(H/A))

if '__main__' == __name__:
    resolve()