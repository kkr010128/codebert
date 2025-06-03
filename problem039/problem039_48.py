string = input()
a, b, c = map(int, (string.split(' ')))
if a < b & b < c :
    print('Yes')
else:
    print('No')
