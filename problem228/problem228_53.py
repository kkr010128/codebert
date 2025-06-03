H = int(input())
a = 1
i = 1
while a < H:
    a += 2 ** i
    i += 1
print(a)