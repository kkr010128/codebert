n, x, t = map(int, input().split())
if n % x == 0:
    m = n // x
else:
    m = (n // x) +1
j = m * t
print(j)
