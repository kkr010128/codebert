N = int(input())
A = list(map(int, input().split()))
A_all = A[0]
for i in range(1,N):
    A_all ^= A[i]
B = [0] * N
for j in range(N):
    B[j] = A[j] ^ A_all
print(' '.join(map(str, B)))
