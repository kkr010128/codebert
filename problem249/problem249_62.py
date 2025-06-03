a, b, k = map(int, input().split())

if (a >= k):
    aa = a - k
    bb = b
else:
    aa = 0
    bb = max(0, b - (k - a))

print(aa, bb)
