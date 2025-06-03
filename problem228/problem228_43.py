H = int(input())
a = 1
an = 1
while a < H:
    a *= 2
    if a<=H:
        an += a
    else:
        break
print(an)