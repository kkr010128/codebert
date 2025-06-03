a, b, k = map(int, input().split())
if a > k:
    x = a - k
    y = b
elif a + b > k:
    x = 0
    y = a + b - k
else:
    x = 0
    y = 0
print(int(x), int(y))