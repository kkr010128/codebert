a, b = [int(input()) for _ in range(2)]
c = [1, 2, 3]
c.remove(a)
c.remove(b)
print(*c)