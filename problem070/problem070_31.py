N, M = map(int, input().split())
F = [[] for _ in range(N)]
P = [0] * N
for i in range(M):
    A, B = map(int, input().split())
    F[A-1].append(B-1)
    F[B-1].append(A-1)
c=0
l = []
for i in range(N):
    if P[i] == 0:
        c+=1
        l.append(i)
        while len(l)>0:
            p=l.pop()
            P[p] = c
            for j in F[p]:
                if P[j] == 0:
                    l.append(j)
print(c-1)
