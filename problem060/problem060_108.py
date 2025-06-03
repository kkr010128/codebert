N, M, L = map(int, raw_input().split())
nm = [map(int, raw_input().split()) for n in range(N)]
ml = [map(int, raw_input().split()) for m in range(M)]

ml_t = []
for l in range(L):
    tmp = []
    for m in range(M):
        tmp.append(ml[m][l])
    ml_t.append(tmp)

for n in range(N):
    tmp1 = nm[n]
    col = [0]*L
    for l in range(L):
        tmp2 = ml_t[l]
        for m in range(M):
            col[l] += tmp1[m] * tmp2[m]
    print ' '.join(map(str, col))