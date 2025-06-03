N, M = map(int, input().split())
if N < 2:
    A = 0
else:
    A = int(N * (N - 1) / 2)
if M < 2:
    B = 0
else:
    B = int(M * (M - 1) / 2)

print(A + B)
