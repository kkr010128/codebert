import sys
N, K = map(int, input().split())

if K == 1:
    print(0)
    sys.exit()

a = abs(N - K * (N // K + 1))
print(min(a, abs(a - K)))
