values = input()
a, b = [int(x) for x in values.split()]

print('{0} {1} {2:.5f}'.format(a // b, a % b, a / b))