nA, nB, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = [0] + A
B = [0] + B


X = [[] for _ in range(M)]
Y = [[] for _ in range(M)]
C = [[] for _ in range(M)]

for i in range(M):
    X[i], Y[i], C[i] = map(int, input().split())

# indipendent
ans1 = min(A[1:]) + min(B[1:])

# set
ans2 = max(A) + max(B)
for x, y, c in zip(X, Y, C):
    ans2 = min(ans2, A[x] + B[y] - c)

print(min(ans1, ans2))