import sys

N, A, B = map(int, sys.stdin.readline().split())
if (B - A) % 2 == 0:
    print((B - A) // 2)
else:
    print(min(A + (B - A - 1) // 2, N - B + 1 + (B - A - 1) // 2))