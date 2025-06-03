N, M = map(int, input().split())
C = [-1] * 3


for i in range(M):
    s, c = map(int, input().split())
    if C[s - 1] == -1:
        C[s - 1] = c
    else:
        if C[s - 1] != c:
            print(-1)
            exit()

if N == 1 and (M == 0 or (M == 1 and C[0] == 0)):
    print(0)
    exit()

for i in range(10 ** (N - 1), 10 ** N):
    si = str(i)
    flg = True
    for j in range(N):
        if C[j] != -1 and si[j] != str(C[j]):
            flg = False
            break
    if flg:
        print(i)
        exit()
print(-1)
