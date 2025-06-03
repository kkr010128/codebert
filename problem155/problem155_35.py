N,M = map(int,input().split())
H = list(map(int,input().split()))
bad = []
for i in range(M):
    A,B = map(int,input().split())
    if H[A-1] > H[B-1]:
        bad.append(B-1)
    elif H[A-1] < H[B-1]:
        bad.append(A-1)
    else:
        bad.append(A-1)
        bad.append(B-1)
print(N-len(set(bad)))