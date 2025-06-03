values = input()
a, b = [int(x) for x in values.split()]
if a == b:
    print('a == b')
elif a > b:
    print('a > b')
else:
    print('a < b')