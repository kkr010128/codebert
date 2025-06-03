def resolve():
    N, X, Y = list(map(int, input().split()))
    X -= 1
    Y -= 1
    dists = [[0 for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            dists[i][j] = min(j-i, abs(X-i)+abs(Y-j)+1)
    counts = [0 for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            counts[dists[i][j]] += 1
    for i in range(1, N):
        print(counts[i])


if '__main__' == __name__:
    resolve()