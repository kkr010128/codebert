M = int(input())
A = [int(_) for _ in input().split()]
N = 1000
kabu = 0
if A[0] < A[1]:
    kabu, N = divmod(N, A[0])
for a, b, c in zip(A, A[1:], A[2:]):
    if a <= b >= c:
        N += kabu * b
        kabu = 0
    elif a >= b <= c:
        dkabu, N = divmod(N, b)
        kabu += dkabu
N += kabu * A[-1]
print(N)
