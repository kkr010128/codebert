def compare(a, b):
    if a > b:
        print('a > b')
    elif a < b:
        print('a < b')
    else:
        print('a == b')

a, b = [int(x) for x in input().split()]
compare(a, b)