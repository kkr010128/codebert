n = int(input())

p = 10
a = 0
if n % 2 == 0:
    while p <= n:
        a += n // p
        p *= 5
print(a)