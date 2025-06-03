N, M, L = map(int, raw_input().split())
nm = [map(int, raw_input().split()) for n in range(N)]
ml = [map(int, raw_input().split()) for m in range(M)]

for n in range(N):
    col = [0] * L
    for l in range(L):
        for m in range(M):
            col[l] += nm[n][m] * ml[m][l]
    print ' '.join(map(str, col))