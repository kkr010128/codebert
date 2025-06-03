s, t = input().split()
a, b = map(int, input().split())
u = input()

if s == u:
    x = a - 1
    y = b
else:
    x = a
    y = b - 1

print(x, y)
