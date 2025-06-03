while 1:
    n = int(input())
    if n == 0:
        break
    L = list(map(int, input().split()))
    mean = sum(L) / len(L)
    V = sum((s - mean) ** 2 for s in L) / len(L)
    print(V ** 0.5)