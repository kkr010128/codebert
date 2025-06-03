
N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()

if N % 2 == 0:
    l = A[N // 2 - 1] + A[N // 2]
    u = B[N // 2 - 1] + B[N // 2]
    print(u - l + 1)
else:
    l = A[N // 2]
    u = B[N // 2]
    print(u - l + 1)
