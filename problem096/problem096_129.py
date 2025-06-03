n = input()
n = n.split()
d = int(n[1])
n = int(n[0])
c = 0
for a in range(n):
    b = input()
    b = b.split()
    x = int(b[0])
    y = int(b[1])
    if x * x + y * y <= d * d:
        c = c + 1
print(c)