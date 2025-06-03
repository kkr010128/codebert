N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

A = [a for a, b in AB]
B = [b for a, b in AB]

A.sort()
B.sort()

if N % 2:
    ma = B[N // 2]
    mi = A[N // 2]
else:
    ma = B[N // 2 - 1] + B[N // 2]
    mi = A[N // 2 - 1] + A[N // 2]

print(ma - mi + 1)