a, b, k = list(map(int, input().split()))

if a >= k:
    a -= k
elif b >= k-a:
    b -= k-a
    a = 0
else:
    a = b = 0
print(a, b)