N = int(input())
A = list(map(int, input().split()))
B = []
R = 0
L = sum(A)
for i in range(N):
  B.append(abs(L-R))
  R += A[i]
  L -= A[i]
print(min(B))