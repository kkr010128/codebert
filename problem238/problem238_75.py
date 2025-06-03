N, K, S = map(int, input().split())
L = []
if (S < 10**9):
    for i in range(K):
        L.append(str(S))
    for i in range(N - K):
        L.append(str(S + 1))
elif (S == 10 ** 9):

    for i in range(K):
        L.append(str(S))
    for i in range(N - K):
        L.append(str(1))
print(' '.join(L))
