n, a, b = map(int, input().split())
x = int(n / (a + b))
y = n - ((a + b) * x)
if y >= a:
    z = a
else:
    z = y
print(int((a * x) + z))