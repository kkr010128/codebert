def resolve():
    import math as m
    N = int(input())
    nn = m.ceil(N / 1.08)
    if m.floor(nn * 1.08) == N:
        print(nn)
    else:
        print(":(")


resolve()
