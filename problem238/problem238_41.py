N, K, S = map(int ,input().split())


if N == K:
    A = [S] * N
elif S == 10**9:
    A = [S]*K + [1]*(N-K)
elif K == 0:
    A = [S+1] * N
elif S == 1:
    A = [1]*K + [2]*(N-K)
else:
    A = [S+1] * N
    x = S // 2
    y = S - x
    for i in range(K+1):
        if i%2 == 0:
            A[i] = x
        else:
            A[i] = y

print(' '.join(map(str, A)))