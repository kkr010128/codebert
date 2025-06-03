n = int(input())
out = ''
for i in range(3,n+1):
    if i % 3 == 0:
        out += ' {0}'.format(i)
        continue
    elif i % 10 == 3:
        out += ' {0}'.format(i)
        continue
    n = i
    while n // 10:
        n = n // 10
        if n % 10 == 3:
            out += ' {0}'.format(i)
            n = 0
print(out)