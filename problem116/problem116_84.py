a = input()
b = input()
c = 0
d = 0
for x in a:
    if x != b[c]:
        d += 1
    c += 1
print(d)