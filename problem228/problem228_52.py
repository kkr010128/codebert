h = int(input())
p = 1
i = 1

while h > 1:
    h = h // 2
    p += 2 ** i
    i += 1

print(p)