def resolve():
    A, B = list(map(int, input().split()))
    import math
    for i in range(1, math.ceil(100/0.08)+1):
        if math.floor(i*0.08) == A and math.floor(i*0.1) == B:
            print(i)
            return
    print(-1)


if '__main__' == __name__:
    resolve()