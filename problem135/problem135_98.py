a, b = map(str, input().split(' '))
a = int(a)
b = int(''.join(b.split('.')))
print(a*b//100)