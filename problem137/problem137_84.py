N = int(input())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()

if N % 2 == 1:
    M = B[N // 2]
    m = A[N // 2]
    print(M - m + 1)

else:
    M = (B[N // 2 - 1] + B[N // 2]) / 2
    m = (A[N // 2 - 1] + A[N // 2]) / 2
    print(int((M - m + 0.5) * 2))
