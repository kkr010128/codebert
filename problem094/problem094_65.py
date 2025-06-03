import sys
input = sys.stdin.readline
R, L, K = map(int, input().split())
V = [0]*(R*L)
for _ in range(K):
    r, c, v = map(int, input().split())
    V[(c-1)*R+(r-1)] = v
A, B, C, D = [[0]*(R+1) for _ in range(4)]
for i in range(L):
    for j in range(R):
        A[j] = max(A[j-1],B[j-1],C[j-1],D[j-1])
        v = V[i*R+j]
        if v != 0:
            D[j], C[j], B[j] = max(C[j]+v,D[j]), max(B[j]+v,C[j]), max(A[j]+v,B[j])
print(max(A[-2],B[-2],C[-2],D[-2]))