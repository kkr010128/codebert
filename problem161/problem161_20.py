A, B, N = map(int, input().split())
if N >= B - 1:
    x = B - 1
    c = (A * x) // B - A * (x // B)
else:
    x = N
    c = (A * x) // B - A * (x // B)
print(c)