x, y, z = map(int, input().split())
x, y = y, x
x, z = z, x
print(str(x) + ' ' + str(y) + ' ' + str(z))
