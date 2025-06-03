def resolve():
    A, B, N = list(map(int, input().split()))
    x = min(B-1, N)
    import math
    print(math.floor(A*x/B))


if '__main__' == __name__:
    resolve()
