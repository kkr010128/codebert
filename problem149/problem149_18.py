class book:
    def __init__(self, C, A):
        self.C = C
        self.A = A
N, M, X = [int(i) for i in input().split()]
P = []
for i in range(N):
    tmp = [int(i) for i in input().split()]
    C = tmp.pop(0)
    P.append(book(C, tmp))

learn = [0 for i in range(M)]
minc = 10**7
flag = 0
for i in range(2 ** N):
    csum = 0
    for j in range(M):
        learn[j] = 0
    for j in range(N):
        if ((i >> j) & 1):
            csum += P[j].C
            for k in range(M):
                learn[k] += P[j].A[k]
    if min(learn) >= X:
        flag = 1
        if minc > csum:
            minc = csum
if flag == 1:
    print(minc)
else:
    print(-1)

