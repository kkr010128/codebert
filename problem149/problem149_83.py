N, M, X = map(int, input().split())
I = [list(map(int, input().split())) for i in range(N)]
C = [0] * N
A = [[0] * M] * N
for i in range(N):
    C[i] = I[i][0]
    A[i] = I[i][1:]
ans = -1
anslist = []

for i in range(2**N):
    flag = 0
    c = 0
    total = [0] * M
    for j in range(N):
        if ((i >> j) & 1):
            c += C[j]
            for k in range(M):
                total[k] += A[j][k]
    for k in range(M):
        if total[k] < X:
            flag = 1
            break
    if flag == 1:
        continue
    anslist.append(c)

if len(anslist) != 0:
    anslist.sort()
    ans = anslist[0]

print(ans)