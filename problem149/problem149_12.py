N, M, X = map(int,input().split())
C = []
A = []
for _ in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)

ans = -1
for i in range(2**N):
    c = 0
    R = [0 for _ in range(M)]
    for j in range(N):
        if (i>>j) % 2:
            c += C[j]
            for m in range(M):
                R[m] += A[j][m]
    flag = True
    for m in range(M):
        if R[m] < X:
            flag = False
            break
    if flag:
        if ans == -1:
            ans = c
        elif ans > c:
            ans = c

print(ans)