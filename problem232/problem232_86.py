a, b = input().split()
na = int(a)
nb = int(b)

sa = a * nb
sb = b * na

print(sa if sa < sb else sb)
