A, B, K = map(int, input().split())
if A >= K:
    a = A - K
    b = B
else:
    if K <= A + B:
        a = 0
        b = B - (K - A)
    else:
        a = 0
        b = 0
print(a, b)
