N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = []
C = []
for q in range(Q):
    b, c = map(int, input().split())
    B.append(b)
    C.append(c)

sam = sum(A)
baketu = [0]*(100001)
for a in A:
    baketu[a] += 1

for q in range(Q):
    sam = sam + baketu[B[q]] * (C[q] - B[q])
    baketu[C[q]] += baketu[B[q]]
    baketu[B[q]] = 0
    #print(baketu)
    print(sam)