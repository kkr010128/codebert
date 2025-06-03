n, x, t = [int(n) for n in input().split(' ')]
a = n // x * t
if n % x != 0:
    a += t
print(a)
