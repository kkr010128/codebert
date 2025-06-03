N, P = map(int, input().split())
S = input()

XX = 0
if P == 2:
    for i in range(N):
        if int(S[i]) % 2 == 0:
            XX += i + 1
    print(XX)
elif P == 5:
    for i in range(N):
        if int(S[i]) % 5 == 0:
            XX += i + 1
    print(XX)
else:
    base = 1
    X = [0 for i in range(N)]
    X[-1] = int(S[-1])
    for i in range(N, 0, -1):
        X[i-1] = (base * int(S[i-1])) % P
        base *= 10
        base %= P
    for i in range(1, N):
        X[i] += X[i-1]
        X[i] %= P
    D = {i: 0 for i in range(P)}
    D[0] = 1
    for i in range(N):
        D[X[i]] += 1
    XX = 0
    for i in D:
        XX += (D[i] * (D[i] - 1)) // 2
    print(XX)