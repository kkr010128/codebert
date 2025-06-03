x = [int(s) for s in input().split()]
(a, b) = (x[0], x[1])

if a == b:
    print('a == b')
elif a < b:
    print('a < b')
else:
    print('a > b')