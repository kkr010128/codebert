N, K = map(int, input().split())
A = [int(i) for i in input().split()]

for _ in range(K):
    flg = True
    imos = [0]*(N+1)
    for i in range(N):
        imos[max(0, i-A[i])] += 1
        imos[min(N, i+A[i]+1)] -= 1
    A = [0]*N
    c = 0
    for i in range(N):
        c += imos[i]
        A[i] = c
        if c != N:
            flg = False
    if flg is True:
        print(*([N]*N), sep=' ')
        exit()


print(*A)
