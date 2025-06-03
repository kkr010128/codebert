def resolve():
    N, M, X = list(map(int, input().split()))
    C = []
    A = []
    for i in range(N):
        ins = list(map(int, input().split()))
        C.append(ins[0])
        A.append(ins[1:])
    minprice = float("inf")
    for bits in range(1<<N):
        comps = [0 for _ in range(M)]
        price = 0
        for odr in range(N):
            if (bits & (1<<odr)):
                price += C[odr]
                for i in range(M):
                    comps[i] += A[odr][i]
        for i in range(M):
            if comps[i] < X:
                break
        else:
            minprice = min(minprice, price)
    print(minprice if minprice < float("inf") else -1)


if '__main__' == __name__:
    resolve()