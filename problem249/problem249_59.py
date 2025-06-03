A, B, K = map(int, input().split())
a = max(0, A - K)
b = B
if K - A > 0:
    b = max(0, B - K + A)
print(a, b)
