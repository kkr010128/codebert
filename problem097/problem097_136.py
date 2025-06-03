def resolve():
    K = int(input())
    N = 7
    c = 1
    for i in range(10**6):
        if N % K == 0:
            print(c)
            break
        else:
            N = N * 10 + 7
            N %= K
            c += 1
    else:
        print(-1)
resolve()