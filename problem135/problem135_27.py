a, b = input().split()
a = int(a)

for i in range(len(b)):
    if b[i] == '.':
        t = 10 ** (len(b)-1-i)
        nb = int(b[:i] + b[i+1:])

print(a*nb//t)