x = raw_input()
a, b, c = x.split()
a = int(a)
b = int(b)
c = int(c)

kai = 0
d = b + 1

for i in range(a, d):
    if c % i == 0:
        kai += 1

print kai