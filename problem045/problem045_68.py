x = input()
a, b = [int(z) for z in x.split()]
x = a // b
y = a % b
z = ('{:.5f}'.format(a / b))

print('{} {} {}'.format(x, y, z))